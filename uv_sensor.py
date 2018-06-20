import time
import Rpi.GPIO as gpio

class UvSensor():
    def __intit__(self):
        gpio.setmode(gpio.Board)
        TRIG = 1
        ECHO = 2
        HIGH_VOL = 3
        LOW_VOL = 4
        gpio.setup(HIGH_VOL,gpio.OUT)
        gpio.setup(LOW_VOL,gpio.OUT)
        gpio.output(HIGH_VOL, gpio.HIGH)
        gpio.output(LOW_VOL, gpio.LOW)
        gpio.setup(TRIG, gpio.OUT)
        gpio.setup(ECHO, gpio.IN)
	self.dist = 0

    def run(self):
	gpio.output(TRIG, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	gpio.output(TRIG, True)
	time.sleep(0.00001)
	gpio.output(TRIG, False)

	while gpio.input(ECHO) == 0:
	    pulse_start = time.time()

	while gpio.input(ECHO) == 1:
  	    pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	self.dist = round(distance, 2)
	return self.dist
