"""
template method pattern
same process(steps), different implementations
"""
import abc


class TemplateBase(metaclass=abc.ABCMeta):

    def template_method(self):
        self._step_1()
        self._step_2()

    @abc.abstractmethod
    def _step_1(self): pass

    @abc.abstractmethod
    def _step_2(self): pass


class ConcreteClass1(TemplateBase):
    def _step_1(self):
        pass

    def _step_2(self):
        pass


class ConcreteClass2(TemplateBase):
    def _step_1(self):
        pass

    def _step_2(self):
        pass
