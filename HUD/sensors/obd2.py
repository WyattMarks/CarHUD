import obd


class OBD2():
    def __init__(self):
        self.sensor = obd.OBD(fast=False, timeout=30)

    def GetSpeed():
        cmd = obd.commands.SPEED
        response = self.sensor.query(cmd)
        self.speed = response.value.to("mph")

        return self.speed

