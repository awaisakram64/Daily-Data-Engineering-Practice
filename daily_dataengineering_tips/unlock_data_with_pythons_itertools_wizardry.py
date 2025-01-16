import itertools

def pairwise_sum(iterable):
    """ Produces pairwise sums from the iterable, like a sliding window of size 2. """
    a, b = itertools.tee(iterable)
    next(b, None)
    return [x + y for x, y in zip(a, b)]

numbers = [1, 2, 3, 4, 5]
print(pairwise_sum(numbers))