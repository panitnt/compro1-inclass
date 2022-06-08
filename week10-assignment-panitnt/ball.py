import math

from vector import Vector
from border import Border
import copy


class Ball:
    """
    Maintains ball objects which can calculate their own movements.
    """

    # add your implementation
    def __init__(self, pos, vel, acc, border=None, color='black'):
        '''
        :param pos: Vector class
        :param vel: Vector class
        :param acc: Vector class
        :param border: Border class
        :param color: string of color
        '''
        self.pos = copy.deepcopy(pos)
        self.vel = vel
        self.acc = acc
        self.border = border
        self.color = color
        self.list = []  # create to use in def draw

    def __repr__(self):
        '''to representation of an object'''
        return f'Ball(pos={self.pos}, vel={self.vel}, acc={self.acc})'

    @property
    def pos(self):
        '''get position'''
        return self.__pos

    @pos.setter
    def pos(self, p):
        '''set position'''
        if not isinstance(p, Vector):
            raise TypeError('pos must be a Vector object')
        self.__pos = copy.deepcopy(p)

    @property
    def vel(self):
        '''get velocity'''
        return self.__vel

    @vel.setter
    def vel(self, v):
        '''set velocity'''
        if not isinstance(v, Vector):
            raise TypeError('vel must be a Vector object')
        self.__vel = copy.deepcopy(v)

    @property
    def acc(self):
        '''get acceleration'''
        return self.__acc

    @acc.setter
    def acc(self, a):
        '''set acceleration'''
        if not isinstance(a, Vector):
            raise TypeError('acc must be a Vector object')
        self.__acc = copy.deepcopy(a)

    @property
    def border(self):
        '''get border'''
        return self.__border

    @border.setter
    def border(self, bor):
        '''set border'''
        if bor is None:
            pass
        elif not isinstance(bor, Border):
            raise TypeError('border must be a Border object')
        else:
            self.__border = copy.deepcopy(bor)
            b_left, b_right, b_bottom, b_top = self.border.sides  # to get sides of border
            ball_x, ball_y = self.pos.x, self.pos.y
            if (b_left <= ball_x) and (ball_x <= b_right) and (b_bottom <= ball_y) and (ball_y <= b_top):
                # this case is not hit a corner
                pass
            else:
                raise ValueError("border must cover the current ball's position")
        self.__border = copy.deepcopy(bor)

    @property
    def color(self):
        '''get color'''
        return self.__color

    @color.setter
    def color(self, col):
        '''set color'''
        if not isinstance(col, str):
            raise TypeError('color must be a string')
        self.__color = col

    def update(self, dt):
        '''to update position, velocity ,and acceleration in every dt'''
        pos, vel, acc = self.pos, self.vel, self.acc
        new_vel = vel + (acc * dt)
        new_pos = pos + (new_vel * dt)
        self.vel, self.pos = new_vel, new_pos
        if self.border is None:
            pass
        else:
            b_left, b_right, b_bottom, b_top = self.border.sides
            if new_pos.x < b_left:  # this case is ball hit left corner
                self.pos.x = (2 * b_left - pos.x) - (vel.x * dt)
                self.vel.x *= -1
            elif new_pos.x > b_right:  # this case is ball hit right corner
                self.pos.x = (2 * b_right - pos.x) - (vel.x * dt)
                self.vel.x *= -1
            elif new_pos.y < b_bottom:  # this case is ball hit bottom corner
                self.pos.y = (pos.y - 2 * b_bottom) - (vel.y * dt)
                self.vel.y *= -1
            elif new_pos.y > b_top:  # this case is ball hit top corner
                self.pos.y = (2 * b_top - pos.y) - (vel.y * dt)
                self.vel.y *= -1
            else:
                self.vel, self.pos = new_vel, new_pos  # this corner is not hit any corner

    def draw(self, painter):
        '''te show ball movement'''
        painter.pensize(2)
        painter.pencolor(self.color)
        painter.penup()
        painter.goto(self.pos.x, self.pos.y)
        self.list.append(self.pos)
        painter.pendown()
        if len(self.list) >= 10:
            num = len(self.list) - 10
        else:
            num = 0
        for i in range(num, len(self.list)):
            painter.goto(self.list[i].x, self.list[i].y)
        painter.dot(15, self.color)


if __name__ == "__main__":
    import doctest

    doctest.testfile("docs/ball.md")
