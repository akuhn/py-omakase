from distutils.core import setup
import pypandoc


long_description = pypandoc.convert('README.md', 'rst')

setup(
  name = 'omakase',
  packages = ['omakase'],
  version = '0.5.0',
  description = 'My personal functions.',
  long_description = long_description,
  author = 'Adrian Kuhn',
  author_email = 'akuhnplus@gmail.com',
  url = 'https://github.com/akuhn/py-omakase',
)
