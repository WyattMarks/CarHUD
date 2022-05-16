from serial.tools import list_ports
from serial import Serial
from time import sleep



## Python class to interpret VK-162 GPS Module serial output
#  Written by Wyatt Marks (wmarks@siue.edu) 05-15-2022
class GPS():
    def __init__(self):
        ports = list_ports.comports()
        self.port = None
        self.coords = None

        for port, desc, hwid in sorted(ports):
                if "GPS/GNSS" in desc:
                    self.port = port
                    break
        
        if self.port == None:
            raise Exception("GPS Not Found")

        self.serial = Serial(self.port, baudrate=9600)

    # GPS Outputs DEGREESMINUTES.MINUTEDECIMAL    I want DEGREES.DEGREESDECIMAL
    def formatDegreesMinutes(self, coordinates, cardinal):
        parts = coordinates.split(b'.')

        if (len(parts) != 2):
            return coordinates
        
        left = parts[0]
        right = parts[1]

        minutes = int(left[-2:].decode("utf-8")) + float(right.decode("utf-8")) / 100000
        degrees = int(left[:-2].decode("utf-8"))

        final = degrees + minutes / 60

        if (cardinal == b'S' or cardinal == b'W'):
            final = -final

        return str(final)

    def ProcessLine(self, data):
        message = data[0:6]
        if (message == b'$GPRMC'): #GPRMC = Recommended minimum specific GPS/Transit data
            parts = data.split(b',')
            if parts[2] == b'V':
                print("GPS receiver warning")
            else:
                print(f"{parts[5]} - {parts[6]}")
                print(f"{parts[3]} - {parts[4]}")
                longitude = self.formatDegreesMinutes(parts[5], parts[6])
                latitude = self.formatDegreesMinutes(parts[3], parts[4])
                self.coords = [str(latitude), str(longitude)]
        else:
            # Ignore any other data, idk what it is anyway
            pass
    
    ## Returns the coordinates in Degree Decimal
    def GetCoords(self):
        while self.serial.in_waiting > 0:
            line = self.serial.readline()
            self.ProcessLine(line)
        

        return self.coords







if __name__ == "__main__":
    gps = GPS()
    while True:
        print(gps.GetCoords())
        sleep(5)