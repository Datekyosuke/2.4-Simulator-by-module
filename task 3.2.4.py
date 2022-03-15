import numpy as np

k= int(input())

mas = []
for i in range(k):
    mas.append(input().split())
mas = np.array(mas, dtype=int)
ygol = np.radians((int(input())))

rot = np.array([[np.cos(ygol), np.sin(ygol)], [-np.sin(ygol), np.cos (ygol)]])
x = np.dot(mas, rot)
avg = np.mean(x, 0)
print("avg_x = %6.2f, avg_y = %6.2f" % (avg[0], avg[1]))