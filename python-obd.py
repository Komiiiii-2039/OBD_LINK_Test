import obd
import time

obd.logger.setLevel(obd.logging.DEBUG)
ports = obd.scan_serial()
print("Available ports: ", ports)
if len(ports) == 0:
    print("No ports found")
    exit()
else:
    print("Using port: ", ports[0])

connection = obd.OBD(portstr=ports[0], protocol="6", baudrate=38400, fast=False, timeout=40, start_low_power=True)

while True:
    cmd = obd.commands.SPEED
    response = connection.query(cmd)
    print(response.value)
    time.sleep(1)