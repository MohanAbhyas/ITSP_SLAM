import RPi.GPIO as gpio
class Controller():
    def __init__(self):
        self.kp = 2
        self.kd = 1
        self.kpr = 2
        self.kdr = 1
        self.prsntState = [0, 0, 0]
        self.setPoint = [0, 0, 0]
        self.maxForce = 10
        self.Output1Pin =
        self.Output2Pin =
        self.GROUND =
        gpio.setmode(gpio.BOARD)
        gpio.setup(Output1Pin, gpio.OUT)
        gpio.setup(Output2Pin, gpio.OUT)
        self.pwm1 = gpio.PWM(Output1Pin, 100)
        self.pwm2 = gpio.PWM(Output2Pin, 100)
    def updateSetpoint(self, prsntState_, setPoint_):
        self.prsntState = prsntState_
        self.setPoint = setPoint_
    def run(self):
        time_start = time.time()
        forwdPrev = 0
        rotPrev = 0
        while True:
            time_end = time.time()
            rotErr = setPoint[2] - prsntState[2]
            if rotErr > 180:
                rotErr -= 360
            elif rotErr <= -180:
                rotErr += 360
            forwdErr = math.sqrt(math.pow(setPoint[0]-prsntState[0],2) +
                            math.pow(setPoint[1]-prsntState[1],2))
            rotForce = kpr*setPoint[2] + kdr*(rotErr-rotPrev)/(time_end - time_start)
            frwdFrce = kp*forwdErr+kd*(forwdErr - frwdPrev)/(time_end - time_start)
            pwm1.ChangeDutyCycle(min((frwdFrce+rotForce)/(2*maxForce),1)*100)
            pwm2.ChangeDutyCycle(min((frwdFrce-rotForce)/(2*maxForce),1)*100)
            rotPrev = rotErr
            frwdPrev = forwdErr
            time_start = time.time()
            time.sleep(0.001)
