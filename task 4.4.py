import numpy as np
from math import sqrt
def V(s, h):
    return 1/3*s**2*h
def PL(s, h):
    return 2*s*sqrt(0.25*s**2+h**2)
do = np.array(input().split(), dtype=float)
vp = np.array(input().split(), dtype=float)
VP = []
PB = []
for i in range((len(do))):
    VP.append(float(V(do[i], vp[i])))
    PB.append(float(PL(do[i], vp[i])))
VP = np.array(VP)
PB = np.array(PB)
maxV = VP.max()
index_maxV = np.argmax(VP)
maxP = PB.min()
index_maxP = np.argmin(PB)
print("Vmax: %2d, %8.2f, Smin: %2d, %8.2f" % (index_maxV, maxV, index_maxP, maxP))