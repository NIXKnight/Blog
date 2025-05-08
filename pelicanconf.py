# Site Author Information
AUTHOR = 'Saad Ali'

# Site General Information
SITENAME = 'NIXKNIGHT'
SITESUBTITLE = 'Not just another NIX admin'

# Content Path
PATH = "content"

# Static paths
STATIC_PATHS = [
  'images',
  'extra',
  'pages',
  'casts'
]

# Plugins Configuration
PLUGINS = [ 'sitemap' ]

# Theme Settings
THEME = 'Dark-Theme'

# Localization Settings
TIMEZONE = 'Asia/Karachi'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL and Save As Configuration for Authors and Categories
AUTHOR_URL = False
AUTHOR_SAVE_AS = False
CATEGORY_URL = False
CATEGORY_SAVE_AS = False

# URL and Save As Configuration for Articles, Tags, and Pages
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
TAGS_SAVE_AS = 'tags/index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DIRECT_TEMPLATES = [ 'index', 'tags' ]

# Markdown Extensions
MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
      'markdown.extensions.extra': {},
      'markdown.extensions.toc': {},
      'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}

# Social widget
SOCIAL = (
  ('twitter', 'https://twitter.com/SaadKnight'),
  ('linkedin', 'https://www.linkedin.com/in/saadali27/'),
  ('github', 'https://github.com/NIXKnight'),
)

# Pagination configuration
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{base_name}/index.html'),
  (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Sitemap Configuration
SITEMAP = {
  "format": "xml",
  'priorities': {
    'indexes': 1.0,
    'articles': 0.8,
    'pages': 0.5,
  },
  'changefreqs': {
    'indexes': 'daily',
    'articles': 'weekly',
    'pages': 'monthly',
  }
}

# Pygments configuration
CODE_HIGHLIGHTER = "pygments"
PYGMENTS_STYLE = 'one-dark'
# optional, for reST blocks only
PYGMENTS_RST_OPTIONS = {"linenos": "table"}   # or "inline", "None", etc.
