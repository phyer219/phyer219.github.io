AUTHOR = 'ZQW'
SITENAME = '从冰上的水'
SITEURL = ""

PATH = "content"
OUTPUT_PATH = 'docs'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

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
STATIC_PATHS = ['.']


SLUGIFY_SOURCE = 'basename'
DEFAULT_CATEGORY = '未分类'
THEME = './themes/universe'
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('首页', '/'),
             ('分类', '/categories.html'),
             ('标签', '/tags.html')
             ]


# ----------------- org_md_zqw_render settings -----------------------------
PLUGINS = ['plugins.org_md_zqw_render', 'plugins.jupyter_zqw']
from markdown_math_escape import MathEscapeExtension
MARKDOWN = {"extension_configs": {'tables': {},
                                  'fenced_code': {},
                                  MathEscapeExtension(delimiters="dollers"): {},
                                  'markdown.extensions.meta': {}
                                  },
            "output_format": "html5"
            }

# add some javascript in SCRIPTS_PATH (for example, MathJax) to
# TEMPLATES_TO_MODIFY, for example, base.html, so all page will changed.
SCRIPTS_PATH = './plugins/org_md_zqw_render/scripts.html'
TEMPLATES_TO_MODIFY = ['base.html']

# ----------------- org_md_zqw_render settings end --------------------------

PLUGINS.append('plugins.sitemap')

# STATIC_PATHS = ['images', 'extra/CNAME']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
