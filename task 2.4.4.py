from math import pow
def anyt(s, n, k, t):
    ka = k/1200
    return ((ka*pow((1+ka),n))/(pow((1+ka),n)-1))*s
def diff(s, n, k, t):
    return s/n + (s-(t-1)*(s/n))*(k/1200)
s = int(input())
n = int(input())
k = int(input())
anyt_list =[float(anyt(s, n, k, t)) for t in range (1, n+1, 1)]
diff_list =[float(diff(s, n, k, t)) for t in range (1, n+1, 1)]
doh_a = sum(anyt_list)-s
doh_d = sum(diff_list)-s
for i in range(n):
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (i+1, diff_list[i], anyt_list[i]))
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (doh_d, doh_a))