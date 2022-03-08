import numpy as np
x_array = np.array(input().split(), dtype=float)
h_array = np.array(input().split(), dtype=float)
a = np.polyfit(x_array, h_array, 2)
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
h_zero = get_trend(0, a)

x_target = float(input())

h_target = float(input())

h_target_v = get_trend(x_target, a)
delta_h = abs(h_target_v - h_target)

if delta_h <= 0.5:

    print("h0 = %6.2f," % h_zero, "yes")

else:

    print("h0 = %6.2f," % h_zero, "no")