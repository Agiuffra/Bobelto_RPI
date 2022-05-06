#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from pyPS4Controller.controller import Controller
from time import sleep

ip_host = '192.168.1.39'

#val_L3_x_old = 0

factory = PiGPIOFactory(host=ip_host)
print("Raspberry IP: " + ip_host)
print(factory.pi_info)
servo = Servo(18,min_pulse_width = 0.6/1000, max_pulse_width = 2.4/1000, pin_factory=factory)


class MyController(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)
		
	def on_L3_left(self,value):
		#print(value, end='\r')
		if (value < 0 and value > (0-32768)):
			servo.value = value/32768
			print("Servo Izq. :" + str(value), end='\r')

	def on_L3_x_at_rest(self):
		print("\nServo Med.", end='\n')
		servo.value = 0

	def on_L3_right(self,value):
		#print(value, end='\r')
		if (value > 0 and value <= 32768): 
			servo.value = value/32768
			print("Servo Der. :" + str(value), end='\r')
			
	def on_circle_press(self):
		print("Servo MIN", end='\r')
		servo.min()
		
	def on_circle_release(self):
		print("Servo MAX", end='\r')
		servo.mid()
		
	def on_square_press(self):
		print("Servo MIN", end='\r')
		servo.max()
		
	def on_square_release(self):
		print("Servo MAX", end='\r')
		servo.mid()

	# Not Used ============================
			
	def on_L3_up(self,value):
		print("", end='\r')

	def on_L3_y_at_rest(self):
		print("", end='\r')

	def on_L3_down(self,value):
		print("", end='\r')

controller = MyController(interface="/dev/input/js2", connecting_using_ds4drv=False)
controller.listen(timeout=60)

