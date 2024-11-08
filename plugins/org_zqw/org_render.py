import os
import shutil
import re
from copy import deepcopy


def clean_dir(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def load_file(path):
    with open(path, 'r') as f:
        res = f.read()
    return res


class Extractor:
    """
    the method `run`: input a Post, we modify the Post.ori_str and Post.meta

    For example:
    Post.ori_str = "#+TITLE: a title demo
                    * a first level title "
    Post.meta = {}

    ==>

    Post.ori_str = "* a first level title"
    Post.meta = {'title': 'a title demo'}
    """
    def __init__(self):
        self.extractors = []
    def addExtractor(self, pattern, name):
        def extractor(post):
            lines = post.ori_str.split('\n')
            def popi(lines):
                for i, l in enumerate(lines):
                    match = re.search(pattern, l)
                    if match:
                        lines.pop(i)
                        post.meta.setdefault(name, []) # for multiline html tags
                        post.meta[name].append(match.group('val').strip())
                        popi(lines)
            popi(lines)
            post.ori_str = '\n'.join(lines)
            return None
        self.extractors.append(extractor)

    def run(self, post):
        for ex in self.extractors:
            ex(post)
        self.prettify_meta(post)

    def prettify_meta(self, post):
        pass


class OrgExtractor(Extractor):
    def __init__(self):
        super().__init__()
        self.addExtractor(r'#\+TITLE\:(?P<val>.*)', 'title')
        self.addExtractor(r'#\+DATE\:(?P<val>.*)', 'date')
        self.addExtractor(r'#\+CATEGORIES\:(?P<val>.*)', 'categories')
        self.addExtractor(r'#\+TAGS\:(?P<val>.*)', 'tags')
        self.addExtractor(r'#\+HTML\:(?P<val>.*)', 'html')

    def prettify_meta(self, post):
        for k in post.meta.keys():
            if k == 'date':
                post.meta[k] = self.prettify_meta_date(post.meta[k][0])
            if k == 'tags':
                post.meta[k] = self.prettify_meta_tags(post.meta[k][0])
    def prettify_meta_date(self, old_date: str) -> list:
        """
        old_date in form of: "<2000-02-20>"
        return a list of int, for example: [2000, 2, 20]
        """
        year = int(old_date[1:5])
        month = int(old_date[6:8])
        day = int(old_date[9:11])
        return [year, month, day]

    def prettify_meta_tags(self, old_tags: str) -> list:
        """
        'BEC, Tc'
        ==>
        ['BEC', 'Tc']
        """
        tags = old_tags.split(',')
        tags = [tag.strip() for tag in tags]
        return tags
# ------------------------------------------------


# ------------------- OrgFilter ---------------
class Filter:
    def addFilter(self, pattern, name):
        def filter(block, renderer):
            if not block.protect:
                block.data = re.sub(pattern, renderer.sub(name), block.data)
            return None
        self.filters.append(filter)

    def run(self, post, renderer):
        for b in post.blocks:
            for f in self.filters:
                f(b, renderer)


class OrgFilter(Filter):
    def __init__(self):
        self.filters = []
        self.addFilter(r'\=(?!\s)(?P<data>.+?)(?<!\s)\=', 'codeinline')
        self.addFilter(r'\*(?!\s)(?P<data>.+?)(?<!\s)\*', 'em')
        self.addFilter(r'(\[\[)(?P<url>http.*?)(\]\]|\]\[(?P<tag>.*?)\]\])', 'url')
        self.addFilter(r'(\[\[)(file:)(?P<path>.*?\.(png|jpg|gif))(\]\]|\]\[(?P<figalt>.*?)\]\])', 'figure')
        self.addFilter(r'(\[\[)(file:)(?P<path>.*?\.(py|mp4))(\]\]|\]\[(?P<tag>.*?)\]\])', 'file')
#-----------------------------------------------

# ------------------ OrgBlocksParser ---------------
class Block:
    protect = False
    bmeta = {}
    def __init__(self, btype, data):
        self.data = data
        self.btype = btype

    def __repr__(self):
        return f'<{self.btype}><{self.data}>'


class BlocksParser:
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    temp.append(b.data)
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                else:
                    temp.append(b.data)
            elif self.start(b):
                inside = True
                temp.append(b.data)
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None


class SignleLineBlocksParser(BlocksParser):
    pattern = ''
    def run(self, post):
        for b in post.blocks:
            if not b.protect:
                match = re.search(self.pattern, b.data)
                if match:
                    b.btype = self.btype
                    b.data = match.group('data')
                    b.block_meta = deepcopy(match.groupdict())


class OrgMathBlocksParser(BlocksParser):
    protect = True
    btype = 'math'
    def start(self, block):
        return re.search(r'\\begin\{align\*?\}', block.data)
    def end(self, block):
        return re.search(r'\\end\{align\*?\}', block.data)


class OrgCodeBlocksParser(BlocksParser):
    protect = True
    btype = 'code'
    def start(self, block):
        return re.search(r'#\+begin_src(?P<lang>.*?$)', block.data,
                         re.IGNORECASE)
    def end(self, block):
        return re.search(r'#\+end_src', block.data,
                         re.IGNORECASE)
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    #temp.append(b.data)
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.bmeta = bmeta
                    nb.protect = self.protect
                    news.append(nb)
                else:
                    temp.append(b.data)
            elif self.start(b):
                inside = True
                bmeta = {'lang': self.start(b).group('lang')}
                #temp.append(b.data)
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None
class OrgQuoteBlocksParser(BlocksParser):
    protect = True
    btype = 'quote'
    def start(self, block):
        return re.search(r'#\+begin_quote', block.data, re.IGNORECASE)
    def end(self, block):
        return re.search(r'#\+end_quote', block.data, re.IGNORECASE)
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                else:
                    temp.append(b.data)
            elif self.start(b):
                inside = True
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None

class OrgTableBlocksParser(BlocksParser):
    protect = True
    btype = 'table'
    def start(self, block):
        return re.search(r'^(\s*\|)', block.data)
    def end(self, block):
        return re.search(r'^(?!\s*\|)', block.data)
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    data = temp
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(b)
                    news.append(nb)
                else:
                    temp.append(b.data.split(r'|'))
            elif self.start(b):
                inside = True
                temp.append(b.data.split(r'|'))
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None

class OrgParagraphBlocksParser(BlocksParser):
    protect = False
    btype = 'paragraph'
    def run(self, post):
        blank = False
        inside = False
        temp = []
        news = []
        for i, b in enumerate(post.blocks):
            if blank and (b.data != '' and b.btype == 'line'):
                # last line blank, this line not blank,
                # that is a start of paragraph!
                inside = True
                temp.append(b.data)
            elif inside:
                if (b.data == '' or b.btype != 'line'
                    or (i+1)==len(post.blocks)):
                    # inside the paragraph, and this line blank or not a line,
                    # this line should not a paragraph, end it!
                    inside = False
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                    news.append(b)
                else: temp.append(b.data)
            else:
                news.append(b)
            if b.data == '' or b.btype != 'line':
                blank = True
            else:
                blank = False
        post.blocks = news
        news = []
        return None

class OrgListBlocksParser(BlocksParser):
    protect = False
    btype = 'list'
    def run(self, post):
        blank = False
        inside = False
        temp = []
        news = []
        for i, b in enumerate(post.blocks):
            if (b.data[:2] == r'- ' and b.btype == 'line') and not inside:
                inside = True
                temp.append(b.data)
            elif inside:
                if ((blank and b.data != '' and b.data[:2] !='- ') or b.btype != 'line'
                     or (i+1)==len(post.blocks)):
                    inside = False

                    data = []
                    for ele in temp:
                        if ele[:2] == '- ':
                            data.append(ele[2:].strip())
                        elif ele != '':
                            data[-1] += ' ' + ele.strip()

                    #data = [li.strip() for li in temp if li !='']
                    #'\n'.join(temp) return a list of str
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                    news.append(b)
                elif b.data != '':
                    temp.append(b.data)

            else:
                news.append(b)
            if b.data == '':
                blank = True
            else:
                blank = False
        post.blocks = news
        news = []
        return None


class OrgHeadingBlocksParser(SignleLineBlocksParser):
    btype = 'heading'
    pattern = r'(^|\s)(?P<level>\*+\s)(?P<data>.*)($|\n)'


class OrgBlockParser:
    def __init__(self):
        self._init_blocksparser()

    def _init_blocksparser(self):
        # order matters! TODO: add a prority!
        self.blocksparsers = []
        self.blocksparsers.append(OrgMathBlocksParser())
        self.blocksparsers.append(OrgCodeBlocksParser())
        self.blocksparsers.append(OrgQuoteBlocksParser())
        self.blocksparsers.append(OrgTableBlocksParser())
        self.blocksparsers.append(OrgHeadingBlocksParser())
        self.blocksparsers.append(OrgListBlocksParser())
        self.blocksparsers.append(OrgParagraphBlocksParser())

    def run(self, post):
        lines = post.ori_str.split('\n')
        post.blocks = [Block('line', l) for l in lines]
        for b in self.blocksparsers:
            b.run(post)


# ----------------------------------

# -------- HTMLRenderer ------------

class Renderer:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)
        else: print('Warning! No Render Method:', prefix + name)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def run(self, post):
        for b in post.blocks:
            name = b.btype
            self.callback('render_', name, b)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return substitution

class HTMLRenderer(Renderer):
    def __init__(self):...
    def render_code(self, block):
        before = f'<pre><code class="language-{block.bmeta["lang"].strip():s}">'
        end = '</code></pre>'
        block.data = block.data.replace(r'<', r'&lt;')
        block.data = block.data.replace(r'>', r'&gt;')
        block.data = before + block.data + end
        return None
    def render_quote(self, block):
        before = '<blockquote>'
        end = '</blockquote>'
        block.data = before + block.data + end
        return None
    def render_table(self, block):
        """block.date is 2D list, which save the table content"""
        before = '<table>\n<tr>\n<td>'
        end = '</td>\n</tr>\n</table>'
        content = ["</td>\n<td>".join(row) for row in block.data]
        content = "</td>\n</tr>\n<tr>\n<td>".join(content)
        block.data = before + content + end
        return None
    def render_math(self, block):
        before = '\n$$'
        end = '$$\n'
        block.data = before + block.data + end
        return None
    def render_paragraph(self, block):
        if block.data[:4] == '<li>':
            return None
        before = '<p>'
        end = '</p>'
        block.data = before + block.data + end
        return None
    def render_heading(self, block):
        level = len(block.block_meta['level'].strip()) + 1
        before = f'<h{level:n}>'
        end = f'</h{level:n}>'
        block.data = before + block.data + end
        return None
    def render_list(self, block):
        li = '<ul>\n'
        for l in block.data:
            li += '<li>' + l + '</li>\n'
        li += '</ul>'
        block.data = li
        return None
    def sub_url(self, match):
        res = f"<a href='{match.group('url'):s}'>"
        if match.group('tag'):
            res += f"{match.group('tag'):s}</a>"
        else:
            res += f"{match.group('url'):s}</a>"
        return res
    # def sub_url(self, match):
    #     return f"<a href='{match.group('url'):s}'>{match.group('tag'):s}</a>"
    def sub_figure(self, match):
        res = f"<p><img src='{match.group('path'):s}'"
        if match.group('figalt'):
            res += f" alt='{match.group('figalt'):s}' max-width:100%><p>"
        else:
            res += " alt='figalt' max-width:100%><p>"
        return res
    def sub_file(self, match):
        res = f"<a href='{match.group('path'):s}'>"
        if match.group('tag'):
            res += f"{match.group('tag'):s}</a>"
        else:
            res += f"{match.group('path'):s}</a>"
        return res
    def sub_codeinline(self, match):
        return f"<code>{match.group('data'):s}</code>"
    def sub_em(self, match):
        return f"<em>{match.group('data'):s}</em>"
    def render_line(self, block):
        if block.data != '':
            print("Warning! There is an unblank Block with btype=line:")
            print('=======', block, '========')
            print('not rendered!')
            return None


# ----------------------------------


class Processor:
    def __init__(self, extractor, filter, parser, renderer):
        self.extractor = extractor
        self.renderer = renderer
        self.filter = filter
        self.parser = parser
        self.temp = []

    def run(self, post):
        # order matters!!!
        self.extractor.run(post)
        self.parser.run(post)
        self.renderer.run(post)
        self.filter.run(post, self.renderer)


class OrgPost:
    def __init__(self, file_path):
        self.ori_str = load_file(file_path)
        self.file_path = file_path
        root_extension = os.path.split(file_path)[-1]
        (self.file_root,
         self.file_extension) = os.path.splitext(root_extension)
        self.meta = {}
        self.html = ''
        # print(self.ori_str)

    def gen_html(self):
        p = Processor(extractor=OrgExtractor(),
                      filter=OrgFilter(),
                      renderer=HTMLRenderer(),
                      parser=OrgBlockParser())
        p.run(self)
        self.html = '\n'.join(b.data for b in self.blocks)


# file = './2023-05-05-physics-damp-drive-oscillator.org'

def convert_to_html(file_path):

    op = OrgPost(file_path)
    try:
        op.gen_html()
    except Exception as e:
        import sys
        import  traceback
        print('fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        print(traceback.print_exc())
        print('..............................')
        raise e
    # print(op.html)
    # print(op.meta)
    # print(op.meta)

    op.meta['title'] = op.meta['title'][0]
    op.meta['date'] = '-'.join([str(i) for i in op.meta['date']])
    op.meta['categories'] = op.meta['categories'][0]
    op.meta['tags'] = ', '.join(op.meta['tags'])
    return op.html, op.meta

# convert_to_html(file)
