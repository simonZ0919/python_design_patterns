"""
visitor pattern
"""
import abc


class Visitable(object):
    def accept(self, visitor):
        visitor.visit(self)


class CompositeVisitable(Visitable):
    def __int__(self, iterable):
        """
        :param iterable: [visitable object]
        """
        self.iterable = iterable

    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)

        visitor.visit(self)


class AbstractVisitor(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def visit(self, element):
        raise NotImplementedError("visit method is not defined")


class ConcreteVisible(Visitable):
    def __init__(self):
        pass


class ConcreteVisitor(AbstractVisitor):
    def visit(self, element):
        pass
