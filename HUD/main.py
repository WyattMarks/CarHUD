from sensors.gps import GPS
from sensors.obd2 import OBD2
from sensors.board import SensorBoard
import pygame
import os
from time import sleep

ON_PI = True

class HUD():

    def __init__(self):
        os.environ["DISPLAY"] = ":0"
        pygame.init()
        self.largeFont = pygame.font.Font(None, 100)
        self.lcd = pygame.display.set_mode((1024, 600), pygame.FULLSCREEN if ON_PI else 0)
        self.lcd.fill((0,0,0))
        pygame.display.update()
        pygame.mouse.set_visible(False)
        self.gps = GPS()
        #self.obd = OBD2()
        self.sensorBoard = SensorBoard()

    def GetTextWidth(self, text, font):
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect()
        return rect.x

    def DrawTextCentered(self, text, font, center, color=pygame.Color(255,255,255)):
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect(center=center)
        if ON_PI:
            flipped = pygame.transform.flip(text_surface, True, False)
            self.lcd.blit(flipped, rect)
        else:
            self.lcd.blit(text_surface, rect)
    
    def DrawTextLeft(self, text, font, topleft, color=pygame.Color(255,255,255)):
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect(topleft=topleft)
        if ON_PI:
            flipped = pygame.transform.flip(text_surface, True, False)
            self.lcd.blit(flipped, rect)
        else:
            self.lcd.blit(text_surface, rect)
        

    def main(self):
        while True:
            self.lcd.fill((0,0,0))

            coords = self.gps.GetCoords()
            if coords != None:
                self.DrawTextCentered(f"Lat: {coords[0]:.5f}, Lon: {coords[1]:.5f}", self.largeFont, (1024/2, 600/3))
            
            speed = 0#self.obd.GetSpeed()
            if speed != None:
                self.DrawTextCentered(f"{speed}mph", self.largeFont, (1024/2, 500))

            brightness = self.sensorBoard.GetBrightness()
            if brightness > 2500:
                self.DrawTextLeft(f"BRIGHT!", self.largeFont, (0, 50))
            elif brightness > 2000:
                self.DrawTextLeft(f"Reasonable!", self.largeFont, (0, 50))
            else:
                self.DrawTextLeft(f"Dark!", self.largeFont, (0, 50))

            pygame.display.update()
            sleep(1)












if __name__ == "__main__":
    hud = HUD()
    hud.main()