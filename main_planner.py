class MainPlanner():
    def __init__(self):
        self.slamObj = Slam()
        self.controller = Controller()
        self.uvf = slamObj.ransac.uv[0]
        self.uvl = slamObj.ransac.uv[1]
        self.frwdDist = 0
        self.leftDist = 0
        self.frwdThresh = 1
        self.leftThresh = 1
        self.turningPoints = []
        self.state = slamObj.state
        self.wallGapleft = 10
        self.wallGapfrwd = 10
        self.botAngle = 0
    def run(self):
        for i in range(0, 10):
            leftDist += uvl.run()
            frwdDist += uvf.run()
        leftDist /= 10
        frwdDist /= 10
        if leftDist > wallGapleft:
            x = slamObj.state[0]
            y = slamObj.state[1]
            botAngle -= 90
            if botAngle < -180:
             botAngle += 360
            stateToBeReached = [x, y, botAngle]
            while abs(slamObj.state[2] - botAngle) > 0.001:
                controller.updateSetPoint(slamObj.state, stateToBeReached)
            self.turningPoints.append([x, y])

        elif frwdDist <= wallGapfrwd:
            x = slamObj.state[0]
            y = slamObj.state[1]
            botAngle += 90
            if botAngle > 180:
             botAngle -= 360
            stateToBeReached = [x, y, botAngle]
            while abs(slamObj.state[2] - botAngle) > 0.001:
                controller.updateSetPoint(slamObj.state, stateToBeReached)
            self.turningPoints.append([x, y])

        elif frwdDist > wallGapfrwd:
            distDiff = frwdDist - wallGapfrwd
            stateToBeReached = [slamObj.state[0] + math.cos(botAngle)*distDiff, slamObj.state[1] + math.sin(botAngle)*distDiff, botAngle]
            controller.updateSetPoint(slamObj.state, stateToBeReached)
