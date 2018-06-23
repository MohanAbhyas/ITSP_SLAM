import math
import numpy as np
class SLAM():
    def __init__(self):
        self.wheel1 = WheelEncoder()
        self.wheel2 = WheelEncoder()
        self.imu = IMU()
        self.uvl = UvSensor()
        self.uvm = UvSensor()
        self.uvr = UvSensor()
        self.state = [0,0,0]
        self.no_of_landMarks = 0
        self.A = ny.array([[1,0,0], [0,1,0], [0,0,1]])
        self.c = 1
        self.p33 = np.array([0,0,0],[ 0,0,0], [0,0,0]])
        self.ransac = Ransac()

    def updateState(self):
        ds = (self.wheel1.output() + self.wheel2.output())/2
        d   t = imu.output()
        dx = ds*math.cos(self.state[2])
        dy = ds*math.sin(self.state[2])
        self.state[0] += dx
        self.state[1] += dy
        self.state[2] += rotation
        A[0][2] = -1*dy
        A[1][2] = dx
        q = ([[c*dx*dx,c*dx*dy,c*dx*dt],[c*dx*dy,c*dy*dy,c*dy*dt],[c*dx*dt,c*dy*dt,c*dt*dt]])
        p33 = np.add(np.dot(np.dot(A,p33),np.transpose(A)) , q)


