k = float(input())
p = float(input())
s = float(input())
k = k*3
m = s*12*p/50
if k<=0 or p<=0 or s<=0:
    print("error")
else:
    if k > m:
        print(round(m, 2))
    else:
        print(round(k, 2))