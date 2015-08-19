
import mraa
import time

print (mraa.getVersion())
x = mraa.Gpio(48)  #MRAA number 48 <=> Edison's GP15
x.dir(mraa.DIR_OUT)

while True:
    print(x.write(1))
    print("x.write(1)")
    time.sleep(1)
    x.write(0)
    print(x.write(0))
    print("x.write(0)")
    time.sleep(1)

