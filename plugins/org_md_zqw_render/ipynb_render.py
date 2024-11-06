from markdown import Markdown
from markdown_math_escape import MathEscapeExtension
import nbformat
from html import escape


class Ipynb:

    def __init__(self, markdown_settings=[]):
        self._md = Markdown(extensions=['tables',
                                                  'fenced_code',
                                                  MathEscapeExtension(delimiters="dollers")])

    def convert_from_file(self, source_path, as_version=4):
        with open(source_path) as f:
            self.notebook = nbformat.read(f, as_version=as_version)
            self.notebook.cells.pop(0) # first cell is metadata
        self.html = self._convert()
        return self.html

    def _convert(self):
        cells = self.notebook.cells
        html_cells = []
        for cell in cells:
            html_cell = self._process_cell(cell)
            html_cells.append(html_cell)
        self.html = '\n'.join(html_cells)
        return self.html

    def _process_cell(self, cell):
        if cell['cell_type'] == 'code':
            return self._process_cell_code(cell)
        if cell['cell_type'] == 'markdown':
            return self._process_cell_markdown(cell)
        if cell['cell_type'] == 'raw':
            return self._process_cell_raw(cell)

    def _process_cell_markdown(self, cell):
        md_str = cell['source']
        html_str = self._md.convert(md_str)
        return html_str

    def _process_cell_code(self, cell):
        code_str = '```python\n' + cell['source'] + '\n```\n'
        code_html = self._md.convert(code_str)
        # print(cell)
        ec = cell['execution_count']
        execution_count = f'<p><pre>In [{ec:n}]</pre></p>'

        outputs = []
        if cell['outputs']:
            try:
                for output in cell['outputs']:
                    text = getattr(output['data'], 'text/plain', '')
                    fig = getattr(output['data'], 'image/png', '')
                    outputs.append('<pre>' + escape(text) + '</pre>')
                    if fig:
                        outputs.append('<img '
                                    + """src=\"data:image/png;base64,"""
                                    + fig
                                   + """\"/>""")
            except Exception:
                import traceback
                traceback.print_exc()
                print('&&&&&&&&&&&&&&&&&&&&&&&&')
                print(output)
                print('&&&&&&&&&&&&&&&&&&&&&&&&')
        return execution_count + code_html + '\n'.join(outputs)

    def _process_cell_raw(self, cell):
        return cell['source']

    def save_html(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.html)
