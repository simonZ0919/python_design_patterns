"""
    decorator pattern
"""
import time


class ProfilingDecorator(object):
    """object with __call__ is equal to function """

    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        start_time = time.time()
        result = self.f(*args)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

        return result


@ProfilingDecorator
def fib(n):
    if n < 2: return

    fibPrev = 1
    fib = 1

    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev

    return fib


if __name__ == '__main__':
    n = 80
    print("Fibonacci number for n={}: {}".format(n, fib(n)))
