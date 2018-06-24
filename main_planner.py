class MainPlanner():
    def __init__(self):
        self.slamObj = Slam()
        self.controller = Controller()
        self.uvf = slamObj.ransac.uv[0]
        self.uvl = slamObj.ransac.uv[1]
        self.frwdDist = 0
        self.leftDist = 0
        self.turningPoints = []
        self.state = slamObj.state
        self.wallGapleft = 10
        self.wallGapfrwd = 10
        self.botAngle = 0
    def run(self):
        for i in range(0, 10):
            self.leftDist += uvl.run()
            self.frwdDist += uvf.run()
        self.leftDist /= 10
        self.frwdDist /= 10
        if self.leftDist > self.wallGapleft:
            x = self.slamObj.state[0]
            y = self.slamObj.state[1]
            self.botAngle -= 90
            if self.botAngle < -180:
                self.botAngle += 360
            stateToBeReached = [x, y, self.botAngle]
            while abs(self.slamObj.state[2] - self.botAngle) > 0.001:
                self.controller.updateSetPoint(self.slamObj.state, stateToBeReached)
            self.turningPoints.append([x, y])

        elif self.frwdDist <= self.wallGapfrwd:
            x = self.slamObj.state[0]
            y = self.slamObj.state[1]
            self.botAngle += 90
            if self.botAngle > 180:
             self.botAngle -= 360
            stateToBeReached = [x, y, self.botAngle]
            while abs(self.slamObj.state[2] - self.botAngle) > 0.001:
                controller.updateSetPoint(self.slamObj.state, stateToBeReached)
            self.turningPoints.append([x, y])

        elif self.frwdDist > self.wallGapfrwd:
            distDiff = self.frwdDist - self.wallGapfrwd
            stateToBeReached = [self.slamObj.state[0] + math.cos(self.botAngle)*distDiff, self.slamObj.state[1] + math.sin(self.botAngle)*distDiff, self.botAngle]
            controller.updateSetPoint(self.slamObj.state, stateToBeReached)
