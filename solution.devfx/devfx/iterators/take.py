import itertools

def take(iterable, n):
    iterator = iter(iterable)
    while True:
        page = list(itertools.islice(iterable, n))     
        if len(page):
            yield page
        else:
            return None
