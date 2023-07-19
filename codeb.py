f = open ('27B.txt')
n = int(f.readline())
minprice = 10**20 #ответ
m = []
area = []
for i in range (n):
    s, a = map(int, f.readline().split())
    area.append(s)
    numofsets = s // 50 if s % 50 == 0 else s // 50 + 1  # количество наборов моющих средств
    numofsets_100_a = int(numofsets * 1.5 * 100) if a == 1 else numofsets * 100
    m.append(numofsets_100_a)
price = 0
higher = 0
lower = 0
for i in range (n): # рассчитываем стоимость уборки, если компания будет на 1 этаже
    numofsets_100_a = m[i]
    price0 = (i + 1) * numofsets_100_a # стоимость для i-ой квартиры
    price += price0
    lower += numofsets_100_a
for i in range (1, n):
    higher += m[i-1]
    lower -= m[i-1]
    price = price + higher - lower
    if 200 - area[i] >= 30: minprice = min(minprice, price)
print(minprice)




