import itertools as it

def circular_iterator(iterable):
    while True:
        for item in iterable:
            yield item