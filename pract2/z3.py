import math

def three(x,y,z):
    up = 1 + math.sin(x+y)**2
    down = abs(x - (2*y) / (1 + x**2 * y**2))
    two = math.cos(math.atan(1/z))**2
    answer = up/down * pow(x, abs(y)) + two
    return answer


x = 3.74 * pow(10, -2)
y = -0.825
z = 0.16 * pow(10, 2)
print(three(x,y,z))
