import numpy as np

path = np.array(input().split(), dtype=int)

speed = np.array(input().split(), dtype=int)

k = int(input())

p = int(input())

path = path[k:p+1]

speed = speed[k:p+1]

len_path = path.sum()

time = path / speed

sum_time = time.sum()

avg_speed = len_path / sum_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, sum_time, avg_speed))