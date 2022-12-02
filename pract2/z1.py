import math

def two(x,y,z):
    up = 2*math.cos(x - 2/3)
    down = 1/2 + math.sin(y)**2
    two = 1 + (z**2 / (3 - z**2 / 5))
    answer = (up/down) * two
    return answer

x = 14.26
y = -1.22
z = 3.5 * pow(10, -2)
print(two(x, y, z))