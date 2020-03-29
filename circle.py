import math
import pygame
import pygame.gfxdraw


class Circle(pygame.sprite.Sprite):
    DEFAULT_RADIUS = 5

    def __init__(self, x, y, r=DEFAULT_RADIUS, color=pygame.Color("black")):
        super().__init__()
        self._x = x
        self._y = y
        self._r = r
        self.color = color

        self.goal_y = None
        self.goal_increments = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = math.ceil(value)

    @property
    def y(self):
        if self.goal_y is None:
            return self._y

        if self.goal_increments is None:
            difference = self.goal_y - self._y
            if abs(difference) <= 1:
                self.goal_y = None
                self.goal_increments = None
                return self._y

            swing_amplitude = math.ceil(difference * 1.35)
            self.goal_increments = (swing_amplitude // 10 for i in range(1, 11))

        try:
            increment = next(self.goal_increments)
        except StopIteration:
            self.goal_increments = None
            return self._y

        self._y += increment
        return self._y

    def draw(self, screen: pygame.Surface):
        pygame.gfxdraw.aacircle(screen, self._x, self.y, self.r, self.color)

    def oscillate(self, goal_y):
        self.goal_y = goal_y
