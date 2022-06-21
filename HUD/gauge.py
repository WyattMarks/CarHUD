import pygame
import math





class Gauge:

    def __init__(self, screen, font, x_cord, y_cord, thickness, radius, color, unit="%"):
        self.screen = screen
        self.font = font
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.thickness = thickness
        self.radius = radius
        self.color = color
        self.unit = unit


    def _drawCircleArc(self, color, startAng, endAng):
        rect = (self.x_cord - self.radius, self.y_cord - self.radius, self.radius*2, self.radius*2)
        pygame.draw.arc(self.screen, color, rect, startAng, endAng, self.thickness)


    def draw(self, percent):
        fill_angle = int(percent*270/100)
        ac = [255-int(self.color[0] * percent/100),
        int(255-self.color[1] * percent/100),
        int(255-self.color[2] * percent/100)]

        pertext = self.font.render(str(percent) + self.unit, True, ac)
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(pertext, pertext_rect)
        for i in range(0, percent, 5):
            self._drawCircleArc(ac, math.pi - math.pi * (i/100), math.pi)
        self._drawCircleArc(ac, math.pi - math.pi * (percent/100), math.pi)
        