# py-omakase

My choice of missing python functions.

    list.len()
    list.map(function)
    list.filter(function)
    list.compact()
    list.uniq()
    list.take(num)
    list.drop(num)
    list.flatten()
    list.each_cons(num)
    list.each_slice(num)
    list.max()
    list.min()
    list.sum()
    list.zip()
    list.first()
    list.last()
    list.freq(function=None)
    list.groupby(function=None)
    list.indexby(function=None)
    list.join(separator)
    list.sortby(function)
    list.sorted()
    list.reduce(function)
    list.reduce(initial, function)
    list.percentile(float)
    list.percentiles(*float)

    tuple.len()
    tuple.map(function)
    tuple.max()
    tuple.min()
    tuple.sum()
    tuple.zip()
    tuple.first()
    tuple.last()
    tuple.freq(function=None)
    tuple.groupby(function=None)
    tuple.indexby(function=None)
    tuple.join(separator)
    tuple.sortby(function)
    tuple.sorted()
    tuple.reduce(function)
    tuple.reduce(initial, function)
    tuple.percentile(float)
    tuple.percentiles(*float)

    dict.len()
    dict.compact()

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
