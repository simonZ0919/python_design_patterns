"""
strategy pattern
"""


def executor(arg1, arg2, func=None):
    if func is None:
        return "Strategy not implemented"

    return func(arg1, arg2)


def strategy_addition(arg1, arg2):
    return arg1 + arg2


def strategy_subtraction(arg1, arg2):
    return arg1 - arg2


def main():
    print(executor(3, 9))
    print(executor(3, 9, strategy_addition))
    print(executor(3, 9, strategy_subtraction))


if __name__ == '__main__':
    main()
