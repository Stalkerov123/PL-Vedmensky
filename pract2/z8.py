import math

def one(x,y,z):
	up = pow(math.e, abs(x-y))*pow(abs(x-y), x+y)
	down = math.atan(x) + math.atan(z)
	one = up / down
	two = pow(pow(x,6)+pow(math.log10(y),2), 1/3)
	answer = one + two
	return answer

x = -2.235*pow(10,-2)
y = 2.23
z = 15.221
print(one(x,y,z))