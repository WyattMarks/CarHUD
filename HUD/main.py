from sensors.gps import GPS

import pygame
import os
from time import sleep

ON_PI = False

class HUD():

    def __init__(self):
        os.putenv('SDL_FBDEV', '/dev/fb1')
        pygame.init()
        self.largeFont = pygame.font.Font(None, 100)
        self.lcd = pygame.display.set_mode((1024, 600), flags = pygame.FULLSCREEN if ON_PI else 0)
        self.lcd.fill((0,0,0))
        pygame.display.update()
        pygame.mouse.set_visible(False)
        self.gps = GPS()

    def main(self):
        while True:
            coords = self.gps.GetCoords()
            if coords != None:
                self.lcd.fill((0,0,0))
                text_surface = self.largeFont.render(f"Lat: {coords[0]:.5f}, Lon: {coords[1]:.5f}", True, pygame.Color(255, 255, 255))
                rect = text_surface.get_rect(center=(1024/2,300/2))
                self.lcd.blit(text_surface, rect)
                pygame.display.update()
                sleep(1)












if __name__ == "__main__":
    hud = HUD()
    hud.main()