"""
    chain of responsibility
"""


class Dispatcher(object):
    def __init__(self, handlers=[]):
        self.handlers = handlers

    def handle_request(self, request):
        for handler in self.handlers:
            request = handler(request)

        return request


def function_1(in_string):
    print(in_string)
    return "".join([x for x in in_string if x != '1'])


def function_2(in_string):
    print(in_string)
    return "".join([x for x in in_string if x != '2'])


def function_3(in_string):
    print(in_string)
    return "".join([x for x in in_string if x != '3'])


def main(request):
    dispatcher = Dispatcher([
        function_1,
        function_2,
        function_3
    ])
    return dispatcher.handle_request(request)


if __name__ == '__main__':
    print(main('1521923136'))
