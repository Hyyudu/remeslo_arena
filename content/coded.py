from utils import camel_to_snake


class Coded:
    @property
    def code(self):
        return camel_to_snake(self.__class__.__name__)