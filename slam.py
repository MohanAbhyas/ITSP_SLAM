import math
import numpy as np
class SLAM():
    def __init__(self):
        self.wheel1 = WheelEncoder()
        self.wheel2 = WheelEncoder()
        self.imu = IMU()
        self.state = [0,0,0]
        self.no_of_landMarks = 0
        self.A = np.array([[1,0,0], [0,1,0], [0,0,1]])
        self.c = 1
        self.p33 = np.array([0,0,0],[ 0,0,0], [0,0,0]])
        self.ransac = Ransac()
        self.H = np.array([0,0,0],[0,0,-1])
        self.R = np.array([0,0],[0,0])
    def UpdateState_Odometry(self):
        ds = (self.wheel1.output() + self.wheel2.output())/2
        dt = imu.output()
        dx = ds*math.cos(self.state[2])
        dy = ds*math.sin(self.state[2])
        self.state[0] += dx
        self.state[1] += dy
        self.state[2] += rotation
        if self.state[2] > 180:
            self.state[2] -= 360
        if self.state[2] <= -180:
            self.state[2] += 360
        self.A[0][2] = -1*dy
        self.A[1][2] = dx
        self.q = ([[c*dx*dx,c*dx*dy,c*dx*dt],[c*dx*dy,c*dy*dy,c*dy*dt],[c*dx*dt,c*dy*dt,c*dt*dt]])
        self.p33 = np.add(np.dot(np.dot(self.A,self.p33),np.transpose(self.A)) , self.q)
        self.p33= np.dot(self.A,self.p33)

    def UpdateState_reobLandmarks(self,lx,ly,n):
        r=
        c=
        b=
        d=
        x = self.state[0]
        y = self.state[1]
        theta = self.state[2]
        r = math.sqrt((x-lx)**2 + (y-ly)**2)
        self.H[0][0]= (x-lx)/r
        self.H[0][1]= (y-ly)/r
        self.H[1][0]= (ly-y)/(r**2)
        self.H[1][1]= (lx-x)/(r**2)
        self.H[0].append(0,0)
        self.H[1].append(0,0)
        self.H[0][2*n+2]= (-1*self.H[0][0])
        self.H[0][2*n+3]= (-1*self.H[0][1])
        self.H[1][2*n+2]= (-1*self.H[1][0])
        self.H[1][2*n+3]= (-1*self.H[1][1])
        self.R[0][0]= r*c
        self.R[1][1]= b*d
        self.K= np.dot(self.P,(np.dot(self.H.transpose(),numpy.linalg.inv(np.add (np.dot(self.H,np.dot(self.P,self.H.transpose())) , np.dot(self.V,np.dot(self.R,self.V.transpose())))))))
        self.X = np.add(self.X, np.dot(self.K,self.z-self.h))


        












