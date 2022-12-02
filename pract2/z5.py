import math

def three(x, y, z):
    one = math.log1p(pow(y, -math.sqrt(abs(x))))
    two = x - y/2
    three = math.sin(math.atan(z))**2
    answer = one*two+three
    return answer

x = -15.246
y = 4.642 * pow(10, -2)
z = 21
print(three(x,y,z))
