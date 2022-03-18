import numpy as np
from math import cos, sin, radians
H = int(input())
T = int(input())
t = float(input())
if 0<=t<=T and T>0:
    f = radians(360*t/T)
    cab_0 = np.array([0,-H/2]) 
    rotate = np.array([[cos(f), sin(f)],[-sin(f), cos(f)]])  
    cab_1 = np.dot(cab_0, rotate)
    cab_1 = cab_1 + H/2
    print("Высота = %6.2f м" % cab_1[1])
else:
    print("error")