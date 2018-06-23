class Controller():
    def __init__(self):
        self.kp = 2
        self.kd = 1
        self.kpr = 2
        self.kdr = 1
        self.prsntState = [0, 0, 0]
        self.setPoint = [0, 0, 0]
    def updateSetpoint(self, prsntState_, setPoint_):
        self.prsntState = prsntState_
        self.setPoint = setPoint_
    def run(self):
        rotErr = setPoint[2] - prsntState[2]
        forwdErr = math.sqrt(math.pow(setPoint[0]-prsntState[0],2) +
                        math.pow(setPoint[1]-prsntState[1],2))*
        rotForce = kpr*setPoint[2]

