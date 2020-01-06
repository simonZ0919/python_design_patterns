"""
proxy pattern
"""
import time


class RawCalculator(object):
    def fib(self, n):
        if n < 2: return 1
        return self.fib(n - 1) + self.fib(n - 2)


def memorize(fn):
    __cache = {}

    def memorized(*args):
        key = (fn.__name__, args)
        if key in __cache:
            return __cache[key]
        __cache[key] = fn(*args)
        return __cache[key]

    return memorized


class CalculatorProxy(object):
    def __init__(self, target):
        self.target = target
        fib = getattr(self.target, 'fib')
        setattr(self.target, 'fib', memorize(fib))

    def __getattr__(self, name):
        return getattr(self.target, name)


if __name__ == '__main__':
    calculator = CalculatorProxy(RawCalculator())

    start_time = time.time()
    fib_sequence = [calculator.fib(x) for x in range(0, 80)]
    end_time = time.time()
    print("calculat length of n={} takes {}", len(fib_sequence), end_time - start_time)
