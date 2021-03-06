import math
import time
import RPi.GPIO as gpio

class WheelEncoder():
    def __init__(self):
        gpio.setmode(gpio.Board)
        HIGH_VOL =1 
        LOW_VOL = 6
        CHANNEL_A = 8
        CHANNEL_B = 10
        gpio.setup(HIGH_VOL, gpio.OUT)
        gpio.setup(LOW_VOL,gpio.OUT)
        gpio.output(HIGH_VOL, gpio.HIGH)
        gpio.output(LOW_VOL, gpio.LOW)
        gpio.setup(CHANNEL_A, gpio.IN)
        gpio.setup(CHANNEL_B, gpio.IN)
        self.distance = 0
        self.factor = 2

    def run(self):
        startTime = time.time()
        readingA_prev = gpio.input(CHANNEL_A)
        readingB_prev = gpio.input(CHANNEL_B)
        while True:
            readingA = gpio.input(CHANNEL_A)
            readingB = gpio.input(CHANNEL_B)
            if readingA != readingA_prev :
                if( (readingA==1 and readingA_prev ==0) and readingB == 1) or( (readingA==0 and readingA_prev== 1) and readingB == 0):
                    self.distance += 1*factor
                else
                    self.distance -= 1*factor
            readingA_prev = readingA
            readingB_prev = readingB
            time.sleep(0.0001)
    def output(self):
        a = self.distance
        self.distance = 0
        return a
