import math

def three(x,y,z):
	one = math.sqrt(x+pow(abs(y),1/4))
	two = pow(pow(math.e,(x-1)/math.sin(z)),1/3)
	answer = pow(2,-x) * one * two
	return answer

x = 3.981*pow(10,-2)
y = -1.625*pow(10,3)
z = 0.512
print(three(x,y,z))