import numpy as np

line_str = input()
line_r = line_str.split()
path = np.array(line_r, dtype=int)
line_sk = input()
line_sk_s = line_sk.split()
speed = np.array(line_sk_s, dtype=int)

len_path = path.sum()

time = path / speed

sum_time = time.sum()

avg_speed = len_path / sum_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, sum_time, avg_speed))