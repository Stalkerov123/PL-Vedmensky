import math

def five(x,y,z):
    up_1 = pow(x, y+1) + pow(math.e, y-1)
    down_1 = 1 + x*abs(y - math.tan(z))
    two = 1 + abs(y-x)
    three = pow(abs(y-x), 2) / 2
    four = pow(abs(y-x), 3) / 3
    answer = (up_1/down_1) * two + three - four
    return answer

x = 2.444
y = 0.869 * pow(10, -2)
z = -0.13 * pow(10, 3)
print(five(x,y,z)) 

