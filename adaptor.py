"""
    adapter pattern
"""


class WhatIHave(object):
    def provided_function_1(self): pass

    def provided_function_2(self): pass


class WhatIWant(object):
    def required_function(self): pass


class ObjectAdapter(object):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def required_function(self):
        return self.what_i_have.provided_function_1()

    def __getattr__(self, item):
        # Other attribute is handled by what_i_have
        return getattr(self.what_i_have, item)


class ClientObject(object):
    def __init__(self, what_i_want):
        self.what_i_want = what_i_want

    def do_something(self):
        self.what_i_want.required_function()


if __name__ == '__main__':
    adapter = ObjectAdapter(WhatIHave())
    client = ClientObject(adapter)
    client.do_something()
