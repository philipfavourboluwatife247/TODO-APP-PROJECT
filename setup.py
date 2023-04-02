try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My ToDo App',
    'author': 'Paul John',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'rainson.work@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ToDo App'],
    'scripts': [],
    'name': 'ToDo App'
}

setup(**config)
