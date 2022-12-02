import math

def two(x,y,z):
    one = pow(abs(math.cos(x) - math.cos(y)), 1 + 2*math.sin(y)**2)
    two = 1 + z + z**2 / 2 + z**3 / 3 + z**4 / 4
    answer = one*two
    return answer

x = 0.4 * pow(10, 4)
y = -0.875
z = -0.475 * pow(10, -3)
print(two(x,y,z))
