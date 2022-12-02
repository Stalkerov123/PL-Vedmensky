import math

def two(x,y,z):
	one = pow(x,y/x) - pow(y/x,1/3)
	up = math.cos(y) - z/(y-x)
	down = 1 + pow(y-x,2)
	two = (y-x) * up / down
	answer = one + two
	return answer

x = 1.825*pow(10,2)
y = 18.225
z = -3.298*pow(10,-2)
print(two(x,y,z))