"""
    decorator pattern
"""
import time
from functools import wraps


class ProfilingDecorator(object):
    """
    decorator class
    object with __call__ is equal to function
    """

    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        start_time = time.time()
        result = self.f(*args)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

        return result


def profiling_decorator_with_unit(unit):
    def profiling_decorator(f):
        """
        decorator function
        :param f: callback function
        :return: decorate function
        """
        # inner.__name__ = f.name
        print("inside decorator")

        @wraps(f)
        def inner(n):
            start_time = time.time()
            # function callback
            result = f(n)
            end_time = time.time()
            print("inner function: ", inner.__name__)
            if unit == "seconds":
                print("[Time elapsed for n = {}] {}".format(n, (end_time - start_time) / 1000))
            # return value to original frame
            return result

        return inner
    return profiling_decorator


# fib = (profiling_decorator_with_unit("second"))(fib)
@profiling_decorator_with_unit("seconds")
def fib(n):
    if n < 2: return
    fibPrev, fib = 1, 1

    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev

    return fib


if __name__ == '__main__':
    n = 80
    print("Fibonacci number for n={}: {}".format(n, fib(n)))
