import math

def four(x,y,z):
    one = 5*math.atan(x)
    two = 1/4 * math.acos(x)
    up = x+3 * abs(x-y) + x**2
    down = abs(x-y)*z + x**2
    answer = one - two * up/down
    return answer

x = 0.1722
y = 6.33
z = 3.25 * pow(10, -4)
print(four(x,y,z))
