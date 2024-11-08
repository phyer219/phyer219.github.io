from pelican import signals
from pelican.readers import BaseReader
from .org_render import convert_to_html


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


def add_reader(readers):
    readers.reader_classes['org'] = OrgReader


def register():
    signals.readers_init.connect(add_reader)
