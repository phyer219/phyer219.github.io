from markdown import Markdown
import nbformat
from html import escape


class Ipynb:

    def __init__(self, markdown_settings={}):
        self._md = Markdown(**markdown_settings)

    def convert_from_file(self, source_path, as_version=4):
        with open(source_path) as f:
            self.notebook = nbformat.read(f, as_version=as_version)
            self.notebook.cells.pop(0)   # first cell is metadata
        self.html = self._convert()
        return self.html

    def _convert(self):
        cells = self.notebook.cells
        html_cells = []
        for cell in cells:
            try:
                html_cell = self._process_cell(cell)
                html_cells.append(html_cell)
            except Exception:
                import traceback
                print('&&&&&&& ipynb_render traceback &&&&&&&&&&')
                traceback.print_exc()
                print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
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
        ec = cell['execution_count']
        if ec:
            ec = f'In [{ec:n}]'
        else:
            ec = 'In [ ]'
        execution_count = '<p><pre>' + ec + '</pre></p>'

        outputs = []
        if cell['outputs']:
            outputs.append(self._process_outputs(cell['outputs']))
        return execution_count + code_html + '\n'.join(outputs)

    def _process_cell_raw(self, cell):
        return cell['source']

    def _process_outputs(self, outputs):
        outputs_html = []
        for output in outputs:
            if output["output_type"] == 'excute_result':
                exec_count = output['execution_count']
                output_html = f'<p><pre>Out [{exec_count:n}]</pre></p>'
                output_html += self._process_output_data(output['data'])
                outputs_html.append(output_html)
            elif output["output_type"] == 'display_data':
                output_html = self._process_output_data(output['data'])
                outputs_html.append(output_html)
            elif output["output_type"] == 'stream':
                outputs_html.append(self._process_output_text(output["text"]))
        return '\n'.join(outputs_html)

    def _process_output_data(self, output_data):
        output_data_html = []
        text = getattr(output_data, 'text/plain', '')
        fig = getattr(output_data, 'image/png', '')
        output_data_html = '<pre>' + escape(text) + '</pre>'
        if fig:
            output_data_html += ('<img '
                                 + """src=\"data:image/png;base64,"""
                                 + fig
                                 + """\"/>""")
        return output_data_html

    def _process_output_text(self, output_text):
        return '<pre>' + escape(output_text) + '</pre>'

    def save_html(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.html)
