import math
import time
import RPi.GPIO as gpio

class WheelEncoder():
    def __init__(self):
        gpio.setmode(gpio.Board)
        HIGH_VOL = 1
        LOW_VOL = 2
        CHANNEL_A = 3
        CHANNEL_B = 4
        gpio.setup(HIGH_VOL, gpio.OUT)
        gpio.setup(LOW_VOL,gpio.OUT)
        gpio.output(HIGH_VOL, gpio.HIGH)
        gpio.output(LOW_VOL, gpio.LOW)
        gpio.setup(CHANNEL_A, gpio.IN)
        gpio.setup(CHANNEL_B, gpio.IN)
        self.vel = 0
        self.factor = 2

    def run(self):
        startTime = time.time()
        readingA_prev = gpio.input(CHANNEL_A)
        readingB_prev = gpio.input(CHANNEL_B)
        try:
            while true:
                readingA = gpio.input(CHANNEL_A)
                readingB = gpio.input(CHANNEL_B)
                if readingA != readingA_prev :
                    timeDiff = time.time()-startTime
                    vel = self.factor/timeDiff
                    startTime = time.time()
                    if (readingA-readingA_prev > 1 and readingB > 1) or (readingA-readingA_prev < -1 and readingB < 1):
                        self.vel = vel
                    else
                        self.vel = -vel
                readingA_prev = readingA
                readingB_prev = readingB
        except KeyboardInterrupt:
            gpio.cleanup()

    def output(self)
        return self.vel

