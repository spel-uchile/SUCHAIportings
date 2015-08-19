
import serial
import time

ser = serial.Serial('/dev/ttyMFD1', 9600)

ind = 0
while True:
    ser.write("hola mundo %s\n" % ind)
    print("hola mundo %s" % ind)
    time.sleep(2)
    msg = ser.readline()
    print(msg)
    ind += 1

