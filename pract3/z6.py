a, b = int(input()), int(input())

if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = a**2

print(x)