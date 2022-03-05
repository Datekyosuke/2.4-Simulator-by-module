str_en = input()
n = int(input())
a = float(input())
b = float(input())
sum_e =0 
line_str = str_en.split()
en = [int(x) for x in line_str]
for d in en:
    if d>n:
        sum_e += n*a+(d-n)*b
    else:
        sum_e += d*a
count = sum(en)
print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (count, sum_e))