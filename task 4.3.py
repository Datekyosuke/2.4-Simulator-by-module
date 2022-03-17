import numpy as np

path = np.array(input().split(), dtype=int)
kol = np.array(input().split(), dtype=int)
p = sum(path)
k=0
for i in range (len(path)):
    inter = np.ceil(kol[i]/path[i])
    if inter <= 30:
        k = k+1
    elif inter >= 31 and inter < 60:
        k += 1.5
    elif inter >= 61 and inter < 120:
        k += 3
    elif inter > 120:
        k += 4.5
print("Длина пути: %3d км, оплата: %5.2f S$" % (p, k))