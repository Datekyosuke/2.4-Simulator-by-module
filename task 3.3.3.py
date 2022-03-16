import numpy as np
y_array = np.array(input().split(), dtype=int)
d_array = np.array(input().split(), dtype=float)
a = np.polyfit(y_array, d_array, 2)
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
ygol = float(input())

d_target = get_trend(ygol, a)

print("Дальность: %6.2f м" % d_target)