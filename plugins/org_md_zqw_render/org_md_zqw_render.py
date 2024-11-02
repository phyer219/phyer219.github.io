from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open
from .org_render import convert_to_html
from markdown import Markdown
from pelican.readers import MarkdownReader
from jinja2 import ChoiceLoader, DictLoader, PrefixLoader
from nbconvert.exporters import HTMLExporter
import nbformat


class OrgReader(BaseReader):
    """Reader for Org files"""
    enabled = True
    file_extensions = ['org']

    def _parse_metadata(self, meta):
        if 'categories' in meta:
            meta['category'] = meta['categories']
        output = {key: self.process_metadata(key, value)
                  for key, value in meta.items()}
        return output

    def read(self, source_path):
        content,  original_meta = convert_to_html(source_path)
        metadata = self._parse_metadata(original_meta)
        return content, metadata


class IpynbReader(BaseReader):
    """Reader for Org files"""
    enabled = True
    file_extensions = ['ipynb']

    def _parse_metadata(self, meta):
        if 'categories' in meta:
            meta['category'] = meta['categories']
        output = {key: self.process_metadata(key, value)
                  for key, value in meta.items()}
        return output

    def read(self, source_path):
        default_template_name = 'plugins/org_md_zqw_render/my_jupyter_template'
        template_name = default_template_name

        with open(source_path) as f:
            nb = nbformat.read(f, as_version=4)
        original_meta = nb.cells[0].metadata
        metadata = self._parse_metadata(original_meta)
        print(original_meta)
        exporter = HTMLExporter(theme='dark',
                                template_name=template_name)
        content, _ = exporter.from_notebook_node(nb)
        return content, metadata


class MyMDReader(MarkdownReader):
    """
    Reader for Markdown files
    """
    def _format_metadata(self, meta):
        if 'tags' in meta:
            meta['tags'][0] = meta['tags'][0].strip('[]')
        if 'categories' in meta:
            meta['category'] = meta['categories']
        return meta

    def read(self, source_path):
        """Parse content and metadata of markdown files"""
        self._source_path = source_path
        self._md = Markdown(**self.settings["MARKDOWN"])
        with pelican_open(source_path) as text:
            content = self._md.convert(text)
        if hasattr(self._md, "Meta"):
            original_meta = self._md.Meta
            original_meta = self._format_metadata(original_meta)

            metadata = self._parse_metadata(original_meta)
        else:
            metadata = {}
        return content, metadata


def add_reader(readers):
    for ext in OrgReader.file_extensions:
        readers.reader_classes[ext] = OrgReader
    readers.reader_classes['md'] = MyMDReader
    readers.reader_classes['ipynb'] = IpynbReader


def modify_template(generator):
    """
    Modify the template of the pelican site.
    """
    default_script_path = 'org_md_zqw_render/scripts.html'
    default_template_to_modify = ['base.html']

    script_path = generator.settings.get('SCRIPTS_PATH',
                                         default_script_path)
    template_to_modify = generator.settings.get('TEMPLATES_TO_MODIFY',
                                                default_template_to_modify)

    with open(script_path) as f:
        new_template = f.read()

    loader_new = DictLoader({t: "{% extends '!old/" + t + "' %}" + new_template
                             for t in template_to_modify})
    loader_old = generator.env.loader
    generator.env.loader = ChoiceLoader([loader_new,
                                         PrefixLoader({"!old": loader_old}),
                                         loader_old])


def register():
    signals.generator_init.connect(modify_template)
    signals.readers_init.connect(add_reader)
