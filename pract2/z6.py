import math

def two(x, y, z):
    one = math.sqrt(10 * (pow(x, 1/3) + pow(x, y+2)))
    two = math.asin(z)**2 - abs(x-y)
    answer = one*two
    return answer

x = 16.55 * pow(10, -3)
y = -2.75
z = 0.15
print(two(x,y,z))