def freq(function, sequence):
    freq = {}
    for each in sequence:
        key = function(each)
        freq[key] = freq.get(key, 0) + 1
    return freq
