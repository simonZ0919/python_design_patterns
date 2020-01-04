"""
    builder pattern
"""

from abc import ABCMeta, abstractmethod


class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class AbstractFormBuilder(object, metaclass=ABCMeta):

    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass


class HtmlForm(object):
    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return "<form>{}</form>".format("".join(self.field_list))


class HtmlFormBuilder(AbstractFormBuilder):

    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{}:<br><input type="text" name="{}"><br>'.format(
                field_dict['label'], field_dict['field_name']))

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(
                button_dict['text']))


class FormDirector(Director):

    def __init__(self):
        Director.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            if field["field_type"] == "button":
                self._builder.add_button(field)


if __name__ == '__main__':
    director = FormDirector()
    director.set_builder(HtmlFormBuilder())

    field_list = [
        {
            "field_type": "text_field",
            "label": "label1",
            "field_name": "field1"
        },
        {
            "field_type": "button",
            "text": "Done"
        }]
    director.construct(field_list)
    print(director.get_constructed_object())
