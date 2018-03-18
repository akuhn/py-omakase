from expects import *


import omakase


def test____should_join_strings():
    words = "the quick brown fox jumps over the lazy dog".split()
    string = words.join(', ')

    expect(string).to(equal('the, quick, brown, fox, jumps, over, the, lazy, dog'))


def test____should_count_elements():
    words = "the quick brown fox jumps over the lazy dog".split()
    num = words.len()

    expect(num).to(be(9))


def test____should_map_elements():
    words = "the quick brown fox jumps over the lazy dog".split()
    array = words.map(len)

    expect(array).to(equal([3, 5, 5, 3, 5, 4, 3, 4, 3]))


def test____should_filter_elements():
    words = "the quick brown fox jumps over the lazy dog".split()
    array = words.filter(lambda each: len(each) < 4)

    expect(array).to(equal('the fox the dog'.split()))


def test____should_sortby_function():
    words = "the quick brown fox jumps over the lazy dog".split()
    array = words.sortby(len)

    expect(array).to(equal('the fox the dog over lazy quick brown jumps'.split()))


def test____should_remove_null_elements():
    sequence = [1, 2, None, None, 3]
    array = sequence.compact()

    expect(array).to(equal([1, 2, 3]))


def test____should_count_element_frequency():
    words = "the quick brown fox jumps over the lazy dog".split()
    freq = words.freq()

    expect(freq['the']).to(be(2))
    expect(freq['quick']).to(be(1))


def test____should_count_frequency():
    words = "the quick brown fox jumps over the lazy dog".split()
    freq = words.freq(len)

    expect(freq[3]).to(be(4))
    expect(freq[4]).to(be(2))
    expect(freq[5]).to(be(3))


def test____should_group_by_element():
    words = "the quick brown fox jumps over the lazy dog".split()
    group = words.groupby()

    expect(group['the']).to(equal('the the'.split()))
    expect(group['quick']).to(equal(['quick']))



def test____should_group_by_mapping():
    words = "the quick brown fox jumps over the lazy dog".split()
    group = words.groupby(len)

    expect(group[3]).to(equal('the fox the dog'.split()))
    expect(group[4]).to(equal('over lazy'.split()))
    expect(group[5]).to(equal('quick brown jumps'.split()))


def test____should_index_by_element():
    words = "the quick brown fox jumps over the lazy dog".split()
    index = words.indexby()

    expect(index['the']).to(equal('the'))
    expect(index['quick']).to(equal('quick'))



def test____should_index_by_mapping():
    words = "the quick brown fox jumps over the lazy dog".split()
    index = words.indexby(len)

    expect(index[3]).to(equal('the'))
    expect(index[4]).to(equal('over'))
    expect(index[5]).to(equal('quick'))


def test____should_remove_duplicates():
    words = "the quick brown fox jumps over the lazy dog".split()
    array = words.uniq()

    expect(array).to(equal('the quick brown fox jumps over lazy dog'.split()))


def test____should_keep_first_few_elements_only():
    words = "the quick brown fox jumps over the lazy dog".split()

    expect(words.take(3)).to(equal('the quick brown'.split()))
    expect(words.take(9000)).to(equal(words))


def test____should_remove_first_few_elements():
    words = "the quick brown fox jumps over the lazy dog".split()

    expect(words.drop(7)).to(equal('lazy dog'.split()))
    expect(words.drop(9000)).to(equal([]))


def test____should_get_first_element():
    words = "the quick brown fox jumps over the lazy dog".split()

    expect(words.first()).to(equal('the'))
    expect([].first()).to(be_none)


def test____should_get_last_element():
    words = "the quick brown fox jumps over the lazy dog".split()

    expect(words.last()).to(equal('dog'))
    expect([].last()).to(be_none)
