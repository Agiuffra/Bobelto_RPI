from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
#kit.serv

# -1 es 0 grados /// 1 es 180 grados
# 0 grados = MINIMA VELOCIDAD
# 180 grados = MAXIMA VELOCIDAD

while (True) :
    kit.continuous_servo[0].throttle = -1
    time.sleep(2)
    print("kk1")
    kit.continuous_servo[0].throttle = 0
    time.sleep(2)
    print("kk2")
    kit.continuous_servo[0].throttle =  1
    time.sleep(2)
    print("kk3")