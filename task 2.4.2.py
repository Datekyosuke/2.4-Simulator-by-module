from math import pow, sqrt
def compute_distance(x, y, x_k, y_k):
    return sqrt(pow((x-x_k),2)+pow((y-y_k),2))
a = input()
b = input()
k = int(input())
r = int(input())
line_x_str = a.split()
line_y_str = b.split()
list_avg = []
line_x = [int(x) for x in line_x_str]
line_y = [int(x) for x in line_y_str]
x_k = line_x[k]
y_k = line_y[k]
n = len(line_x)
distance = [compute_distance(line_x[i], line_y[i], x_k, y_k) for i in range(n)]
count = 0
for d in distance:
    if d<r:
        count = count +1
print(count)