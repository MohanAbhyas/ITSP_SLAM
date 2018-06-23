class Ransac()
    def __init__(self):
        self.state = [0,0,0]
        self.uv[3] = [UvSensor(), UvSensor(), UvSensor()]
        self.listX = []
        self.listY = []
        self.landMarks = []
    def updateState(self, state_):
        self.state[0] = state_[0]
        self.state[1] = state_[1]
        self.state[2] = state_[2]
    def takeReading(self):
        for i in range(0,3):
            val = self.uv[i].run()
            if len(self.list) == 10:
                del self.listX[0]
                del self.listY[0]
            self.listX.append(self.state[0] + val*math.cos(self.state[2]))
            self.listY.append(self.state[1] + val*math.sin(self.state[2])
        landmark = bestFitLine()
        if len(landmark) != 0:
            landmarks.append(landmark)
    def bestFitLine(self):
        coeff[2] = np.polyfit(self.listX, self.listY, 1)
        optimalX = []
        optimalY = []
        for i in range(0,len(self.listX)):
            if abs(listY[i] - coeff[0]*listX[i]- coeff[1]) < 0.1:
                optimalX.append(listX[i])
                optimalY.append(listY[i])
        if len(optimalX) > 2:
            newCoeff[2] = np.polyfit(optimalX, optimalY, 1)
            optimalX.sort()
            if newCoeff[0] > 0:
                optimalY.sort()
            else:
                optimalY.sort(reverse=True)
            return [optimalX[0],optimalY[0],optimalX[-1],optimalY[-1]]
        return []
