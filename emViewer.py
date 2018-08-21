import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as D3
from array import array
import numpy as np
import random as rand

""""FIGURE OUT ERROR HANDLING FOR FUNCTIONS"""

class const(object):
    """ADD MORE CONSTANTS"""
    k = 8.99 * np.power(10, 9)
                
class pointCharge(object):
    """UPDATE DOCUMENTATION / LEARN TENSOR CALCULUS"""
    q = 0
    p = 0
    
    def __init__(self, charge, pvector):
        self.q = charge
        self.p = pvector

          
class vector(object):
    """ADD CROSS/DOT/REFLECT/INVERT FUNCTIONS/OVERLOADS"""
    x = 0
    y = 0
    z = 0
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "<%f, %f, %f>" % (self.x, self.y, self.z)
    
    def __str__(self):
        return "<%f, %f, %f>" % (self.x, self.y, self.z)
    
    def __mul__(self, a):
        if type(a) in (int, float):
            return vector(a*self.x, a*self.y, a*self.z)
    def __rmul__(self, a):
        if type(a) in (int, float):
            return vector(a*self.x, a*self.y, a*self.z)
        
    def mag(self):
       return np.sqrt(np.power(self.x,2) + np.power(self.y,2) + np.power(self.z,2))
    
    def hat(self):
        return vector(self.x/self.mag(), self.y/self.mag(), self.z/self.mag())
        
        
class shell(object):
    x=0
    
class solid(object):
    def __init__(self, shape, dimensions, center):
        return "boop bop finish this"
    x=0
    
def makeCharge(charge, pvector):
    pCharge = pointCharge(charge, pvector)
    return pCharge

def plotCharges(chargeArray):
    """FIGURE OUT BETTER GRAPHICAL SOLUTION / INSTALL BACKEND"""
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    for charges in chargeArray:
        if charges.q > 0:
            ax.scatter(charges.p.x, charges.p.y, charges.p.z, c = "red")
        elif charges.q < 0:
            ax.scatter(charges.p.x, charges.p.y, charges.p.z, c = "blue")
        else:
            ax.scatter(charges.p.x, charges.p.y, charges.p.z, c = "grey")
    return fig

def coulombsLaw(charge, r):
    """"CHECK FOR ACCURACY"""
    return const.k * charge.q/r.mag() * r.hat()



#Plot Random Charges

randArray = []
numCharges = 100
plt.figure()
plt.ion()

for i in range(0, numCharges-1):
    k = vector(rand.uniform(-10,10), rand.uniform(-10,10), rand.uniform(-10,10))
    j = makeCharge(rand.uniform(-3 * 10**-9, 3*10**-9), k)
    randArray.append(j)
    print (coulombsLaw(j, vector(1, 1, 1)))
    
fig = plotCharges(randArray)
fig.show()
