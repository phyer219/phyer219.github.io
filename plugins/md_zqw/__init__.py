from pelican import signals
from pelican.utils import pelican_open
from markdown import Markdown
from pelican.readers import BaseReader


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
        self._md = Markdown(**self.settings["MARKDOWN_ZQW"])
        with pelican_open(source_path) as text:
            content = self._md.convert(text)

        meta = getattr(self._md, "Meta", None)
        metadata = self._parse_metadata(meta)

        return content, metadata


def add_reader(readers):
    readers.reader_classes['md'] = MyMDReader


def register():
    signals.readers_init.connect(add_reader)
