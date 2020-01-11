"""
iterator pattern
iterable object: __iter__ , __next__
generator: execute when call __next__ and stop at yield
module: import itertools
"""
import itertools


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MyTree(object):
    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        current = self.root

        while True:
            if node.data <= current.data:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

    def __iter__(self):
        """
        first find left nodes
        :return: iterable object(must defines __next__ )
        """
        self.stack = [] if self.root is None else [self.root]
        current = self.root
        while current.left is not None:
            current = current.left
            self.stack.append(current)
        return self

    def __next__(self):
        """
        add right nodes to stack
        :return: next item for iterable object
        :raise: StopIteration(no more items)
        """
        if len(self.stack) <= 0:
            raise StopIteration
        while len(self.stack) > 0:
            current = self.stack.pop()
            data = current.data

            if current.right is not None:
                current = current.right
                self.stack.append(current)

                while current.left is not None:
                    current = current.left
                    self.stack.append(current)

            return data

        raise StopIteration


def gen_squares(n):
    i = 0
    while i < n:
        yield i * i
        i += 1


if __name__ == '__main__':
    tree = MyTree(Node(12))
    tree.add_node(Node(3))
    tree.add_node(Node(8))
    tree.add_node(Node(10))
    tree.add_node(Node(16))
    tree.add_node(Node(6))
    tree.add_node(Node(20))
    tree.add_node(Node(15))

    print([x for x in tree if x % 2 == 0])
    # chain two iterator
    print(list(itertools.chain([1, 2, 3], range(6, 9))))

    g = gen_squares(6)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())


