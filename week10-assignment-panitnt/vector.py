import math
import copy


class Vector:
    """Define a vector in 2D space."""

    # add your implementation
    def __init__(self, x=0, y=0):
        '''
        :param x: int/float of x
        :param y: int/float of y
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''to representation of an object'''
        return f'Vector(x={self.x}, y={self.y})'

    @property
    def x(self):
        '''get x'''
        return self.__x

    @x.setter
    def x(self, x1):
        '''set x'''
        if not isinstance(x1, (int, float)):
            raise TypeError('The x attribute must be a number')
        self.__x = x1

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, y1):
        '''set y'''
        if not isinstance(y1, (int, float)):
            raise TypeError('The y attribute must be a number')
        self.__y = y1

    def length(self):
        '''calculate length'''
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def dot(self, other):
        '''to summarize two vector by dot product'''
        return (self.x * other.x) + (self.y * other.y)

    def __add__(self, other):
        '''to add two vector function'''
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''to subtract two vector function'''
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        '''to multiply vector with number function'''
        new_vex = copy.copy(self)
        new_vex.x, new_vex.y = new_vex.x * other, new_vex.y * other
        return new_vex

    def __rmul__(self, other):
        '''to multiply vector with number function'''
        new_vex = copy.copy(self)
        new_vex.x, new_vex.y = new_vex.x * other, new_vex.y * other
        return new_vex


if __name__ == "__main__":
    import doctest

    doctest.testfile("docs/vector.md")
