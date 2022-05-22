import sys
import smbus2 as smbus
import time

PCA9685_ADDRESS = 0x7F
SERVO0 = 0x06
FREQ = 50
NEUTRAL_PULSE = 1500
MAX_PULSE = 2100
MIN_PULSE = 900

I2Cbus = smbus.SMBus(1)

with smbus.SMBus(1) as I2Cbus:
	I2Cbus.write_i2c_block_data(PCA9685_ADDRESS, 0x00, [0x31])
	time.sleep(0.001)
	
	prescalar = (25000000 / (4096 * FREQ * 0.92)) - 1
	
	I2Cbus.write_i2c_block_data(PCA9685_ADDRESS, 0xFE, [byte(prescalar)])
	time.sleep(0.001)
	
	I2Cbus.write_i2c_block_data(PCA9685_ADDRESS, 0x00, [0xA1])
	time.sleep(0.001)
	
	I2Cbus.write_i2c_block_data(PCA9685_ADDRESS, 0x01, [0x04])
	time.sleep(0.001)
	
	pulse_us = 1500 # us
	servoNum = 0

	while(1):
		period_us = 1000000/FREQ
		count = (pulse_us/period_us) * 4096

		LSB = byte(count)
		MSB = byte(count) >> 8

		I2Cbus.write_i2c_block_data(PCA9685_ADDRESS, SERVO0 + (4 * servoNum), [0x00, 0x00, LSB, MSB])
		time.sleep(0.001)
		
		
		
