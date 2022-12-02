import math

def two(x,y,z):
    up = pow(y + pow(x-1, 1/3), 1/4)
    down = abs(x-y) * (math.sin(z)**2 + math.tan(z))
    answer = up/down
    return answer

x = 17.421
y = 10.365 * pow(10, -3)
z = 0.828 * pow(10, 5)
print(two(x,y,z))

