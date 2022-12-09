import random


class ProduceChars:
    """generator class to produce random numbers in a given range"""
    def _init_(self, start, stop):
        self.start = start
        self.stop = stop

    def _iter_(self):
        current = self.start
        while current < 15:
            yield random.randrange(self.start, self.stop)
            current += 1