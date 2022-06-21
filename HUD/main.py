import pygame
import os
from time import sleep
import random
from gauge import Gauge

ON_PI = False
IN_CAR = False

class HUD():

    def __init__(self):
        self.time = 0
        os.environ["DISPLAY"] = ":0"
        if IN_CAR:
                x = True
                while x:
                        try:
                                self.obd = OBD2()
                                print(self.obd.GetSpeed())
                                x = False
                        except:
                                sleep(random.randrange(0, 5))
        pygame.init()
        self.largeFont = pygame.font.Font(None, 60)
        self.smallFont = pygame.font.Font(None, 40)
        self.lcd = pygame.display.set_mode((1024, 600), 0)#pygame.FULLSCREEN)
        self.lcd.fill((0,0,0))
        pygame.display.update()
        pygame.mouse.set_visible(False)
        #self.gps = GPS()
        #self.sensorBoard = SensorBoard()
        self.fuelgauge = Gauge(self.lcd, self.smallFont, 910, 485, 10, 50, pygame.Color(0,0,0))

    def GetTextWidth(self, text, font):
        text_surface = font.render(text, True, pygame.Color(0,0,0))
        rect = text_surface.get_rect()
        return rect.x

    def DrawTextCentered(self, text, font, center, color=pygame.Color(255,255,255)):
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect(center=center)
        self.lcd.blit(text_surface, rect)
    
    def DrawTextLeft(self, text, font, topleft, color=pygame.Color(255,255,255)):
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect(topleft=topleft)
        self.lcd.blit(text_surface, rect)

    def main(self):
        while True:
            self.lcd.fill((0,0,0))
            
            speed = 30#self.obd.GetSpeed()
            if speed != None:
                self.DrawTextCentered(f"{speed}mph", self.largeFont, (1024/2, 500))


            # fuel data
            fuelPressure = 0
            self.DrawTextLeft(f"Fuel Pressure: {fuelPressure} kilopascal", self.largeFont, (0, 50))

            fuelLevel = 50
            self.fuelgauge.draw(fuelLevel)
            self.DrawTextLeft(f"Fuel Level", self.largeFont, (800, 500))

            fuelRate = 0
            self.DrawTextLeft(f"Fuel Rate: {fuelRate} liters/hour", self.largeFont, (0, 150)) # convert units?

            # engine data
            coolantTemp = 0 
            self.DrawTextLeft(f"Coolant Temp: {coolantTemp} degrees", self.largeFont, (0, 250)) # default value in degrees celcius (convert?)
          
            engineLoad = 0
            self.DrawTextLeft(f"Engine Load: {engineLoad}%", self.largeFont, (0, 200))

            engineRPM = 0
            self.DrawTextLeft(f"RPM: {engineRPM}%", self.largeFont, (0, 300))

            engineRunTime = 0
            self.DrawTextLeft(f"Engine Time: {engineRunTime}%", self.largeFont, (0, 350))

            # temperatures
            ambientTemp = 30#self.obd.GetAmbientTemp()
            self.DrawTextLeft(f"Car Temp: {ambientTemp} degrees", self.largeFont, (0, 400)) # default value in degrees celcius (convert?)

            # odometer data
            distanceTraveled = 0
            self.DrawTextLeft(f"Distance: {distanceTraveled} km", self.largeFont, (0, 450)) # convert units?

            self.DrawTextLeft("OFF SCREEN", self.largeFont, (1024, 250))
            
            if ON_PI:
              self.lcd.blit(pygame.transform.flip(self.lcd, True, False), (0,0))
            pygame.display.update()
            sleep(1)













if __name__ == "__main__":
    hud = HUD()
    hud.main()