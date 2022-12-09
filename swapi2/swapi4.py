import random

class Simple:
    foo = []

from timing import timeit

@timeit

def produce_characters(start=1, stop=82):
    return (random.randrange(1, stop=82) for item in range(1, 16))


if __name__ == "__main__":
    print(__name__)