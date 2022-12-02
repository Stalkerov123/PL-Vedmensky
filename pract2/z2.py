import math

def two(x,y,z):
    up = pow(9 + (x-y), 1/3)
    down = x**2 + y**2 + 2
    two = pow(math.e, abs(x-y)) * math.tan(z)**3
    answer = up/down - two
    return answer

x = -4.5
y = 0.75 * pow(10, -4)
z = -0.845 * pow(10, 2)
print(two(x,y,z))
