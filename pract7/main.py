def check_num(n):
    flag = 1
    for _ in str(n):
        if int(_) != 0 and n % int(_) == 0:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        return 1
    return 0

def replace(mas):
    mas[0], mas[-1] = mas[-1], mas[0]
    return mas

l = int(input('длина = '))
mas = []
for i in range(l):
    mas.append(int(input()))
print(*mas)
print(*replace(mas))

print('8.1 ниже')
n = int(input('длина последовательности = '))

for num in range(1, n):
    if check_num(num):
        print(num, end=' ')