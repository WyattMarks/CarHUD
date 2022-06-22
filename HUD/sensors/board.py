from serial.tools import list_ports
from serial import Serial
from time import sleep



## Python class to interpret our Sensor Board serial output
#  Written by Wyatt Marks (wmarks@siue.edu) 05-19-2022
class SensorBoard():
    def __init__(self):
        self.brightness = None
        self.port = "/dev/ttyUSB0"
        self.serial = Serial(self.port, baudrate=115200, timeout=2)

    def GetBrightness(self):
        self.serial.write(b"brightness\n")
        line = self.serial.readline()
        while self.serial.in_waiting > 0:
            line = self.serial.readline()

        if len(line) > 0:
            try:
                self.brightness = int(line)
            except:
                pass

        return self.brightness

    def GetTemperature(self):
        self.serial.write(b"temp\n")
        line = self.serial.readline()
        while self.serial.in_waiting > 0:
            line = self.serial.readline()

        if len(line) > 0:
            try:
                self.temp = int(line) / 100
            except:
                pass

        return self.temp










if __name__ == "__main__":
    board = SensorBoard()
    while True:
        print(f"bright: {board.GetBrightness()}")
        print(f"temp: {board.GetTemperature()}")
        sleep(1)