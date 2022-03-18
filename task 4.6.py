import numpy as np
from math import pow
def get_trend_1(x, a):
    y = a[0]* x + a[1]
    return y
def get_trend_2(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
def get_trend_3(x, a):
    y = a[0] * pow(x,3) + a[1]* x**2 + a[2]*x + a[3]
    return y
strana = str(input())
tur = np.array(input().split(), dtype=float)
k = int(input())
zn = float(input())
g = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
if k ==1:
    a = np.polyfit(g, tur, 1)
    v = get_trend_1(2018, a)
    delta = abs(((v-zn)/zn)*100)
    print("Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц." % (strana, v, delta))
elif k ==2:
    a = np.polyfit(g, tur, 2)
    v = get_trend_2(2018, a)
    delta = abs(((v-zn)/zn)*100)
    print("Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц." % (strana, v, delta))
elif k ==3:
    a = np.polyfit(g, tur, 3)
    v = get_trend_3(2018, a)
    delta = abs(((v-zn)/zn)*100)
    print("Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц." % (strana, v, delta))