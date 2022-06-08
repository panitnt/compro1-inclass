class Student:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    def __repr__(self):
        return f"Student(id='{self.id}', name='{self.name}')"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_set):
        if not isinstance(name_set, str):
            raise TypeError('name must be a string')
        self.__name = name_set


if __name__ == '__main__':
    import doctest
    doctest.testfile('docs/student.md')
