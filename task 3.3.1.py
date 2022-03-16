import numpy as np
import math  as mt
k= int(input())

mas = []
for i in range(k):
    mas.append(input().split())
mas = np.array(mas, dtype = float)
cen = np.mean(mas, 0)
ras =[]
for x in range(k):
    d=mas[x]
    len_line=mt.sqrt(pow((cen[0]-d[0]),2)+pow((cen[1]-d[1]),2))
    ras.append(len_line)
print("центр в точке (%6.3f, %6.3f), r = %6.3f" % (cen[0], cen[1], np.max(ras)))