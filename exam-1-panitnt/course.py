class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.name = name
        self.credits = credits

    def __repr__(self):
        return f"Course(id='{self.id}', name='{self.name}', credits={self.credits})"

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_set):
        if not isinstance(name_set, str):
            raise TypeError('name must be a string')
        self.__name = name_set

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits_set):
        if not isinstance(credits_set, int):
            raise TypeError('credits must be an integer')
        if credits_set <= 0:
            raise ValueError('credits must be positive')
        self.__credits = credits_set


if __name__ == '__main__':
    import doctest
    doctest.testfile('docs/course.md')
