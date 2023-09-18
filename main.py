n1 = int(input('введите начальное число1: '))
n2 = int(input('введите конечное число1: '))
n3 = int(input('введите начальное число2: '))
n4 = int(input('введите конечное число2: '))
measure1 = []
measure2 = []
general = []
while n1 <= n2:
    measure1.append(n1)
    n1 = n1 + n1
while n3 <= n4:
    measure2.append(n3)
    n3 = n3 + 1
for i in measure1:
    for k in measure2:
        if i == k:
            general.append(i)
            break
if len(general) >= 1:
    print('пересечение равно: ', general[0], '-', general[-1])
else:
    print('пересечения между промежутками нет')