from board import SCL, SDA
import busio
import time
from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)
pca.frequency = 50

pca.channels[0].duty_cycle = 0x1333
time.sleep(0.1)
pca.channels[3].duty_cycle = 0x1333
time.sleep(0.1)
pca.channels[4].duty_cycle = 0x1333
time.sleep(0.1)
pca.channels[6].duty_cycle = 0x1333
time.sleep(7)

while(1):
    val_front = 0x0F5C
    val_back  = 0x170A
    pca.channels[0].duty_cycle = val_front
    time.sleep(0.1)
    pca.channels[3].duty_cycle = val_back
    time.sleep(0.1)
    pca.channels[4].duty_cycle = val_front
    time.sleep(0.1)
    pca.channels[6].duty_cycle = val_back
    time.sleep(0.1)
    