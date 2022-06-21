import obd
import logging
from time import sleep

obd.logger.setLevel(obd.logging.DEBUG)

class OBD2():
    def __init__(self):
        self.sensor = obd.OBD(portstr="/dev/rfcomm0", fast=False, timeout=30, baudrate=38400, protocol="6")
        for cmd in self.sensor.supported_commands:
            print(cmd)
        self.sensor.supported_commands.add(obd.commands.SPEED)

    def GetSpeed(self):
        cmd = obd.commands.SPEED
        response = self.sensor.query(cmd)
        self.speed = response.value.to("mph")

        return self.speed

    def GetAmbientTemp(self):
        cmd = obd.commands.INTAKE_TEMP
        response = self.sensor.query(cmd)
        self.temp = response.value

        return self.temp




logging.getLogger().setLevel(logging.DEBUG)

if __name__ == "__main__":
	o = OBD2()
	while True:
		print(o.GetSpeed())
		sleep(1)
		print(o.GetAmbientTemp())
