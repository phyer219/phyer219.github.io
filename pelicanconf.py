AUTHOR = 'ZQW'
SITENAME = '从冰上的水'
SITEURL = ""

PATH = "content"
OUTPUT_PATH = 'docs'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("Github", "https://github.com/phyer219"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# My config -----------------------------------------------------------------
from datetime import datetime
JINJA_GLOBALS = {
    'current_year': datetime.now().year,
}

STATIC_PATHS = ['.']
READERS = {'html': None}
DISPLAY_PAGES_ON_MENU = False

SLUGIFY_SOURCE = 'basename'
DEFAULT_CATEGORY = '未分类'
THEME = './themes/simple-modern'
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'),
            #  ('分类', '/categories.html'),
             ('Physics', '/category/physics'),
             ('Blog', '/category/blog'),
             ('Coding', '/category/coding'),
             ('All', '/archives'),
            #  ('Tags', '/tags.html')
             ]
# My config end -------------------------------------------------------------

# ----------------- My plugins and settings ---------------------------------
# from markdown_math_escape import MathEscapeExtension
MARKDOWN_ZQW = {
    'extensions': ['tables',
                   'fenced_code',
                   'footnotes',
                   'mdx_truly_sane_lists',
                   'markdown_math_escape',
                   'full_yaml_metadata'],
    'extension_configs': {
        'mdx_truly_sane_lists': {'nested_indent': 2},
        },
    'output_format': 'html5'}

PLUGINS = ['plugins.md_zqw',
           'plugins.jupyter_zqw',
           'plugins.org_zqw']

PLUGINS.append('plugins.modify_templates')
SCRIPTS_PATH = './plugins/modify_templates/scripts.html'
TEMPLATES_TO_MODIFY = ['base.html']

PLUGINS.append('plugins.sitemap')
# ----------------- My plugins and settings  end ----------------------------
