class Coded:
    @property
    def code(self):
        return self.__class__.__name__.lower()