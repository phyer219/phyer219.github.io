from pelican import signals
from pelican.utils import pelican_open
from markdown import Markdown
from pelican.readers import MarkdownReader


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
    readers.reader_classes['md'] = MyMDReader


def register():
    signals.readers_init.connect(add_reader)
