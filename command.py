"""
    command pattern
"""


class Invoker(object):
    def __init__(self):
        self.commands = []
        self.undo_stack = []

    def add_command(self, command):
        self.commands.append(command)
        self.undo_stack.append(command)

    def undo(self):
        command = self.undo_stack.pop()
        command["undo"](*command["params"])

    def run(self):
        for command in self.commands:
            command["function"](*command["params"])


if __name__ == '__main__':
    f = lambda string1, string2: print("{} + {} ".format(string1, string2))
    f_undo = lambda string1, string2: print("{} - {} ".format(string1, string2))

    invoker = Invoker()
    invoker.add_command({
        "function": f,
        "undo": f_undo,
        "params": ("Command1", "String1")
    })
    invoker.add_command({
        "function": f,
        "undo": f_undo,
        "params": ("Command2", "String2")
    })

    invoker.run()
    invoker.undo()