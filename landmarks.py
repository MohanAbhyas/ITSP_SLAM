class Ransac()
    def __init__(self):
        self.state = [0,0,0]
        self.uv[3] = [UvSensor(), UvSensor(), UvSensor()]
        self.list = []
    def updateState(self, state_):
        self.state[0] = state_[0]
        self.state[1] = state_[1]
        self.state[2] = state_[2]
    def takeReading(self):
        for i in range(0,3):
            val = self.uv[i].run()
            self.list.append([self.state[0] + val*math.cos(self.state[2]),                                          self

