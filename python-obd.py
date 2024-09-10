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

connection = obd.OBD(portstr=ports[0], fast=False, timeout=40)

#fileに保存
fname = f"log/{time.strftime('%Y%m%d%H%M%S')}.csv"
f = open(fname, 'w')
f.write("time, speed[km/h], rpm\n")
while True:
    t = time.strftime('%Y-%m-%d %H:%M:%S')
    speed = connection.query(obd.commands.SPPED).value
    rpm = connection.query(obd.commands.RPM).value 
    f.write(f"{t}, {speed}, {rpm}\n")
    time.sleep(0.001) #1ms