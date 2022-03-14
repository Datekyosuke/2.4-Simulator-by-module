import numpy as np
def get_trend_2(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
def get_trend_1(x, a):
    y = a[0]* x + a[1]
    return y
x_array = np.array(input().split(), dtype=float)
y_array = np.array(input().split(), dtype=float)
kv = np.polyfit(x_array, y_array, 2)
per = np.polyfit(x_array, y_array, 1)
y1_trend = [get_trend_1(x, per) for x in x_array]
y2_trend = [get_trend_2(x, kv) for x in x_array]
pog1 = [abs((y1_trend-y_array)/y_array) for x in y_array]
pog2 = [abs((y2_trend-y_array)/y_array) for x in y_array]
del_mean1 = np.mean(pog1)
del_mean2 = np.mean(pog2)
if del_mean1 >= del_mean2:
    print("%5.3f %5.3f %5.3f" % (kv[0], kv[1], kv[2]))
else:
    print("%5.3f %5.3f" % (per[0], per[1]))