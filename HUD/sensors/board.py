from serial.tools import list_ports
from serial import Serial
from time import sleep



## Python class to interpret our Sensor Board serial output
#  Written by Wyatt Marks (wmarks@siue.edu) 05-19-2022
class SensorBoard():
    def __init__(self):
        ports = list_ports.comports()
        self.port = None
        self.brightness = None

        for port, desc, hwid in sorted(ports):
            try:
                self.port = port
                self.serial = Serial(self.port, baudrate=115200, timeout=2)
                self.serial.write(b"name\n")
                line = self.serial.readline()
                if line == b"ESP\n":
                    break
            except Exception as e:
                print(e)

        if self.port == None:
            raise Exception("Sensor Board not found!!")

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










if __name__ == "__main__":
    board = SensorBoard()
    while True:
        print(board.GetBrightness())
        sleep(1)