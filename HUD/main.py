from sensors.gps import GPS
from sensors.obd2 import OBD2
import pygame
import os
from time import sleep

class HUD():

    def __init__(self):
        pygame.init()
        self.largeFont = pygame.font.Font(None, 100)
        self.lcd = pygame.display.set_mode((1024, 600))
        self.lcd.fill((0,0,0))
        pygame.display.update()
        pygame.mouse.set_visible(False)
        self.gps = GPS()
        self.obd = OBD2()

    def DrawText(self, text, font, center, color=pygame.Color(255,255,255)):
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect(center=center)
        self.lcd.blit(text_surface, rect)
        

    def main(self):
        while True:
            self.lcd.fill((0,0,0))

            coords = self.gps.GetCoords()
            if coords != None:
                self.DrawText(f"Lat: {coords[0]:.5f}, Lon: {coords[1]:.5f}", self.largeFont, (1024/2, 600/3))
            
            speed = self.obd.GetSpeed()
            if speed != None:
                self.DrawText(f"{speed}mph", self.largeFont, (1024/2, 500))

            pygame.display.update()
            sleep(1)












if __name__ == "__main__":
    hud = HUD()
    hud.main()