from expects import *


import omakase


def test____should_count_elements():
    mapping = { 'red': 34, 'green': 55, 'blue': 89, 'yellow': 144 }

    expect(mapping.len()).to(be(4))


def test____should_remove_null_elements():
    mapping =  { 'red': 34, 'green': 55, 'blue': None, 'yellow': None, 'purple': 233  }
    m = mapping.compact()

    expect(m).to(have_keys('red', 'green', 'purple'))
    expect(m).to(have_len(3))
    expect(m.items()).to(contain(('purple', 233)))

