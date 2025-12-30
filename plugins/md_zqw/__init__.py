import re
from pelican import signals
from pelican.utils import pelican_open
from pelican.readers import BaseReader

from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.texmath import texmath_plugin
import yaml


def render_math_inline(self, tokens, idx, options, env):
    # content 是解析出来的公式纯文本
    content = tokens[idx].content
    return f"${content}$"


def render_math_block(self, tokens, idx, options, env):
    content = tokens[idx].content
    # 块级公式通常建议换行，方便 MathJax 识别
    return f"$$\n{content}\n$$"


class MyMDReader(BaseReader):
    """
    Reader for Markdown files
    """
    enabled = True
    file_extensions = ['md']

    def _parse_metadata(self, meta):
        if not meta:
            return {}
        if 'categories' in meta and 'category' not in meta:
            meta['category'] = meta['categories']

        output = {}
        all_lists = all(isinstance(value, list) for value in meta.values())
        if all_lists:
            return {key: self.process_metadata(key, value)
                    for key, value in meta.items()}

        for key, value in meta.items():
            if hasattr(value, "isoformat") and not hasattr(value, "tzinfo"):
                value = value.isoformat()
            try:
                output[key] = self.process_metadata(key, value)
            except Exception:
                output[key] = value
        return output

    def read(self, source_path):
        """Parse content and metadata of markdown files"""
        self._source_path = source_path
        self._md = MarkdownIt('commonmark', {'breaks': True, 'html': True})
        self._md.use(texmath_plugin, delimiters='dollars')
        self._md.use(texmath_plugin, delimiters='brackets')
        self._md.use(front_matter_plugin)
        self._md.use(footnote_plugin)
        self._md.enable('table')

        self._md.enable(["table", "strikethrough"])

        self._md.add_render_rule("math_inline", render_math_inline)
        self._md.add_render_rule("math_block", render_math_block)

        with pelican_open(source_path) as text:
            text = self._replace_md_links(text)
            tokens = self._md.parse(text)
            html_text = self._md.render(text)

            content = html_text  # self._md.convert(text)

            fm_raw = None
            for t in tokens:
                if t.type == "front_matter":
                    fm_raw = t.content
                    break

        meta = yaml.safe_load(fm_raw) if fm_raw else {}
        metadata = self._parse_metadata(meta)

        return content, metadata

    _LINK_RE = re.compile(r'(\]\()([^\s)]+)(\))')

    def _replace_md_links(self, text):
        def repl(match):
            prefix, url, suffix = match.groups()
            if url.startswith(('http://', 'https://', 'mailto:', '#')):
                return match.group(0)

            base, frag = url, ''
            if '#' in base:
                base, frag = base.split('#', 1)
                frag = f'#{frag}'
            query = ''
            if '?' in base:
                base, query = base.split('?', 1)
                query = f'?{query}'

            # replace the `.md` to `.html`.
            # when refer another post,
            # the html version link should to `html`, not `md`
            if base.endswith('.md'):
                base = f'{base[:-3]}.html'
                return f'{prefix}{base}{query}{frag}{suffix}'
            return match.group(0)

        return self._LINK_RE.sub(repl, text)


def add_reader(readers):
    readers.reader_classes['md'] = MyMDReader


def register():
    signals.readers_init.connect(add_reader)
