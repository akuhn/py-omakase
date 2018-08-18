from expects import *


import omakase


def test____should_cast_as_list():
    words = ('red', 'green', 'blue', 'yellow')

    expect(words.list()).to(equal('red green blue yellow'.split()))


def test____should_join_strings():
    words = ('red', 'green', 'blue', 'yellow')
    string = words.join(', ')

    expect(string).to(equal('red, green, blue, yellow'))


def test____should_count_elements():
    words = ('red', 'green', 'blue', 'yellow')
    num = words.len()

    expect(num).to(be(4))


def test____should_map_elements():
    words = ('red', 'green', 'blue', 'yellow')
    array = words.map(len)

    expect(array).to(equal([3, 5, 4, 6]))


def test____should_sortby_function():
    words = ('red', 'green', 'blue', 'yellow')
    array = words.sortby(len)

    expect(array).to(equal('red blue green yellow'.split()))


def test____should_count_element_frequency():
    words = ('the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')
    freq = words.freq()

    expect(freq['the']).to(be(2))
    expect(freq['quick']).to(be(1))


def test____should_count_frequency():
    words = ('the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')
    freq = words.freq(len)

    expect(freq[3]).to(be(4))
    expect(freq[4]).to(be(2))
    expect(freq[5]).to(be(3))


def test____should_group_by_element():
    words = ('the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')
    group = words.groupby()

    expect(group['the']).to(equal('the the'.split()))
    expect(group['quick']).to(equal(['quick']))



def test____should_group_by_mapping():
    words = ('the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')
    group = words.groupby(len)

    expect(group[3]).to(equal('the fox the dog'.split()))
    expect(group[4]).to(equal('over lazy'.split()))
    expect(group[5]).to(equal('quick brown jumps'.split()))


def test____should_index_by_element():
    words = ('the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')
    index = words.indexby()

    expect(index['the']).to(equal('the'))
    expect(index['quick']).to(equal('quick'))



def test____should_index_by_mapping():
    words = ('the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')
    index = words.indexby(len)

    expect(index[3]).to(equal('the'))
    expect(index[4]).to(equal('over'))
    expect(index[5]).to(equal('quick'))


def test____should_get_first_element():
    words = ('red', 'green', 'blue', 'yellow')

    expect(words.first()).to(equal('red'))
    expect(().first()).to(be_none)


def test____should_get_last_element():
    words = ('red', 'green', 'blue', 'yellow')

    expect(words.last()).to(equal('yellow'))
    expect(().last()).to(be_none)


def test____should_get_minimum():
    words = ('red', 'green', 'blue', 'yellow')

    expect(words.min()).to(equal('blue'))
    expect(().min()).to(be_none)


def test____should_get_maximum():
    words = ('red', 'green', 'blue', 'yellow')

    expect(words.max()).to(equal('yellow'))
    expect(().max()).to(be_none)


def test____should_get_sum():
    sequence = (7, 35, 41, 1, 26, 12)

    expect(sequence.sum()).to(equal(122))
    expect(().sum()).to(equal(0))


def test____should_reduce_to_sum():
    sequence = (7, 35, 41, 1, 26, 12)
    fun = lambda a, b: a + b
    product = lambda a, b: a * b

    expect(sequence.reduce(fun)).to(equal(122))
    expect(().reduce(fun)).to(be_none)
    expect(sequence.reduce(1, product)).to(equal(3134040))
    expect(().reduce(1, product)).to(equal(1))


def test____should_zip():
    a = (7, 35, 41)
    b = (1, 26, 12)

    expect(a.zip(b)).to(equal([(7, 1), (35, 26), (41, 12)]))

