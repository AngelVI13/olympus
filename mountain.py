import pygame
from circle import Circle


class Mountain:
    def __init__(self, points, screen_width: int, screen_height: int, color=pygame.Color("black")):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = color

        self.points = points
        self.points_num = len(points)

        self.circles = []
        padding = screen_width // 20
        for i in range(self.points_num):
            circle_x = (screen_width * i) // self.points_num
            c = Circle(circle_x + padding, screen_height, color=color)
            self.circles.append(c)

        self.trigger_idx = 0

    def trigger_point(self):
        if self.trigger_idx >= self.points_num:
            return

        self.circles[self.trigger_idx].oscillate(goal_y=self.points[self.trigger_idx])
        self.trigger_idx += 1

    def draw(self, canvas: pygame.Surface):
        for idx, circle in enumerate(self.circles):
            circle.draw(canvas)

            if idx < len(self.circles) - 1:
                next_circle = self.circles[idx + 1]
                pygame.draw.aaline(
                    canvas,
                    self.color,
                    (circle.x, circle.y),
                    (next_circle.x, next_circle.y),
                )
