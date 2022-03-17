import numpy as np

time = np.array(input().split(), dtype=int)
for i in range(len(time)):
    if time[i]>60*12:
        print(i)