a = input()
b = input()
sr_v = float(input())
line_0_str = a.split()
line_12_str = b.split()
list_avg = []
line_0 = [float(x) for x in line_0_str]
line_12 = [float(x) for x in line_12_str]
list_avg = [(i+j)/2 for i, j in zip(line_0, line_12)]
for x in range(0, len(line_0), 1):
    if list_avg[x]>sr_v :
        print(x)
    