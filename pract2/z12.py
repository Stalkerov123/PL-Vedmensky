import math

def three(x,y,z):
    one = pow(2, y**x) + pow(3**x , y)
    up = y*(math.atan(z) - 1/3)
    down = abs(x) + 1/(x**2 + 1)
    answer = one + up/down
    return answer

x = 3.251
y = 0.325
z = 0.466 * pow(10, -4)
print(three(x,y,z))
