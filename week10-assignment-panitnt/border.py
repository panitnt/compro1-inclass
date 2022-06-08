import copy
from vector import Vector


class Border:
    """
    Define a border in 2D space with the lower-left corner, width, and height.
    """

    # add your implementation
    def __init__(self, corner, width, height):
        '''
        :param corner: Vector class
        :param width: int/float of width
        :param height: int/float of height
        '''
        self.corner = copy.deepcopy(corner)
        self.width = width
        self.height = height

    def __repr__(self):
        '''to representation of an object'''
        return f'Border(corner={self.corner}, width={self.width}, height={self.height})'

    @property
    def corner(self):
        '''get corner'''
        return self.__corner

    @corner.setter
    def corner(self, c):
        '''set corner'''
        if not isinstance(c, Vector):
            raise TypeError('corner must be a Vector object')
        self.__corner = copy.deepcopy(c)

    @property
    def width(self):
        '''get corner'''
        return self.__width

    @width.setter
    def width(self, w):
        '''set corner'''
        if not isinstance(w, (int, float)):
            raise TypeError('width must be a number')
        if w <= 0:
            raise ValueError('width must be greater than zero')
        self.__width = copy.deepcopy(w)

    @property
    def height(self):
        '''get height'''
        return self.__height

    @height.setter
    def height(self, h):
        '''set corner'''
        if not isinstance(h, (int, float)):
            raise TypeError('height must be a number')
        if h <= 0:
            raise ValueError('height must be greater than zero')
        self.__height = copy.deepcopy(h)

    @property
    def left(self):
        '''get left'''
        return self.corner.x

    @property
    def right(self):
        '''get right'''
        return self.corner.x + self.width

    @property
    def bottom(self):
        '''get bottom'''
        return self.corner.y

    @property
    def top(self):
        '''get top'''
        return self.corner.y + self.height

    @property
    def sides(self):
        '''get sides'''
        left = self.corner.x
        right = self.corner.x + self.width
        bottom = self.corner.y
        top = self.corner.y + self.height
        return left, right, bottom, top

    def draw(self, painter):
        '''to draw the corner'''
        # use the painter object (a turtle) to draw the border
        painter.pencolor('#626396')
        painter.pensize(5)
        painter.penup()
        painter.goto(self.left, self.top)
        painter.pendown()
        painter.goto(self.right, self.top)
        painter.goto(self.right, self.bottom)
        painter.goto(self.left, self.bottom)
        painter.goto(self.left, self.top)


if __name__ == "__main__":
    import doctest

    doctest.testfile("docs/border.md")
