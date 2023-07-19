f = open ('27A.txt')
n = int(f.readline())
minprice = 10**10 #ответ
m = [list(map(int, f.readline().split())) for i in range (n)]
for i in range (n):
    if 200 - m[i][0] >= 30:
        price = 0 #стоимость, если разместить клининг на i-ом этаже
        for j in range (n):
            s, a = m[j]
            numofsets = s//50 if s%50 == 0 else s//50 + 1 #количество наборов моющих средств
            price0 = (abs(i-j)+1)*numofsets*100 #стоимость для j-ой квартиры
            if a == 1: price0 = int(price0*1.5)
            price += price0
        minprice = min(minprice, price)
print(minprice)


