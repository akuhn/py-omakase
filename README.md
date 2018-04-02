# py-omakase

My choice of missing python functions.

    list.len()
    list.map(function)
    list.filter(function)
    list.join(separator)
    list.sortby(function)
    list.compact()
    list.freq(function=None)
    list.groupby(function=None)
    list.indexby(function=None)
    list.uniq()
    list.take(num)
    list.drop(num)
    list.first()
    list.last()
    list.zip()
    list.min()
    list.max()
    list.sum()
    list.reduce(function)
    list.reduce(initial, function)

Examples

    $ python
    >>> import omakase
    >>> array = 'the quick brown fox jumps over the lazy dog'.split()
    >>> array.map(len)
    [3, 5, 5, 3, 5, 4, 3, 4, 3]
    >>> array.filter(lambda each: each > 'hello worlds')
    ['the', 'quick', 'jumps', 'over', 'the', 'lazy']
    >>> array.take(3)
    ['the', 'quick', 'brown']
    >>>

## Installation

To install this package, run

    pip install omakase

## Contributing

Bug reports and pull requests are welcome on github at, https://github.com/akuhn/py-omakase
