from pelican import signals
from pelican.readers import BaseReader
from .ipynb_render import Ipynb
import nbformat


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
        with open(source_path) as f:
            nb = nbformat.read(f, as_version=4)
        original_meta = nb.cells[0].metadata
        metadata = self._parse_metadata(original_meta)
        ipynb = Ipynb(markdown_settings=self.settings["MARKDOWN"])
        content = ipynb.convert_from_file(source_path)
        return content, metadata


def add_reader(readers):
    readers.reader_classes['ipynb'] = IpynbReader


def register():
    signals.readers_init.connect(add_reader)
