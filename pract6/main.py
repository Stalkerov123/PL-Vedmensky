import random as rd

l, mas = int(input('Длина массива = ')), []
for i in range(l):
    mas.append(rd.randint(1, 17))
print(f"Начальный массив: {mas}")

def summ(x):
    result_2 = 0
    for d in x:
        result_2 += d
    return result_2

def average_mean(mas):
    return summ(mas) / len(mas)
def prod(h):
    result = 1
    for i in h:
        result*=i
    return result

print(f"Среднее арифметическое массива = {average_mean(mas)},\
    \nСумма элементов массива = {summ(mas)},\n \
    Произведение элементов массива = {prod(mas)}")
l_2 = int(input('Длина второго массива = '))
mas_2 = []

for u in range(l_2):
    mas_2.append(rd.randint(-3, 3))
print(mas_2)

for i, j in enumerate(mas_2):
    if j == 0:
        mas_2[i] = average_mean(mas_2)
print(*mas_2)

