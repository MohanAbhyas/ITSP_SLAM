import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#instead of BCM

GPIO.setup(2, GPIO.OUT)
#for 5v

GPIO.setup(6, GPIO.OUT)
#for ground

GPIO.output(2, GPIO.HIGH)
#5v

GPIO.output(6, GPIO.LOW)
#ground

GPIO.setup(11, GPIO.IN)
#for channel A

GPIO.setup(12, GPIO.IN)
#for channel B


count=0


def count(x)
	count+=x

try:
	start = time.time()
	timep = 2 # n second
	while(true)
		A = GPIO.input(11)
                B = GPIO.input(11)
                if A != Ap:
                        if B != A:
                                count(+1) #Moving forward
                        else:
                                count(-1) #Moving backward
                         	
		Ap = A
		if time.time() > start + PERIOD_OF_TIME : 
			print(count)
			omega=6.28*count/(timep*ndivisions)
			count=0
			

           
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  



finally:
GPIO.cleanup()
