from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError as error:
    print "\x1b[0;31mImportError: {}\x1b[0m".format(error)
    long_description = None


setup(
  name = 'omakase',
  packages = ['omakase'],
  version = '0.6.1',
  description = 'My personal functions.',
  long_description = long_description,
  author = 'Adrian Kuhn',
  author_email = 'akuhnplus@gmail.com',
  url = 'https://github.com/akuhn/py-omakase',
  install_requires = ['forbiddenfruit'],
)
