import math

def five(x,y,z):
    up_1 = pow(y, x+1)
    down_1 = pow(abs(y-2), 1/3) + 3
    up_2 = x + y/2
    down_2 = 2*abs(x+y)
    two = pow(x+1, -1/math.sin(z))
    answer = up_1/down_1 + up_2/down_2 * two
    return answer

x = 12.3 * pow(10, -1)
y = 15.4
z = 0.252 * pow(10, 3)
print(five(x,y,z))
