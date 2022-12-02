f, v = int(input()), int(input())

if f < 4 and v > 6:
    s = f + v
elif v < 6:
    s = f**2
else:
    s = 2*v

print(s)
