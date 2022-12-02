f, k = int(input()), int(input())

if f < k:
    r =  f + k**2 - 1
elif k < 2 and f == 3:
    r = k**2
else:
    r = f - 1

print(r)

