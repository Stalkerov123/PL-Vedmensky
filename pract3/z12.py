a, b = int(input()), int(input())

if a < b:
    r =  a - b + 1
elif a > b and a > 3:
    r =  b**2 - b
else:
    r = b**2 - 1

print(r)
