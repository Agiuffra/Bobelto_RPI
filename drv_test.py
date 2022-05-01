import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup
#GPIO.cleanup

# Pines de salida (al drv8825)
dirPin = 8
stepPin = 10

GPIO.setup(dirPin,GPIO.OUT)
GPIO.setup(stepPin,GPIO.OUT)

# Constantes
# Direccion = 1 - ADELANTE
# Direccion = 2 - ATRAS
direccion = 2

#Flag = true  (actuar)
#Flag = false (no actuar)
Flag = False

MaxSteps = 6667; # max
#MaxSteps = 6; # max


while True :
    if Flag == True :
        if direccion == 1 :
            GPIO.output(dirPin,True)
            
        elif direccion == 2 :
            GPIO.output(dirPin,False)
            
        for j in range(MaxSteps) :
            GPIO.output(stepPin,True)
            time.sleep(0.001)
            GPIO.output(stepPin,False)
            time.sleep(0.001)
            print(j)
            
        Flag = False
        
        
    else :
        #print("p")
        Flag = input()
        if Flag == "0" :
            Flag = True
        else :
            Flag = False
        
        print(Flag)
        
    


