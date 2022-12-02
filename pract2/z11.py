import math

def four(x,y,z):
	one = pow(y,pow(abs(x),1/3))
	up = abs(x-y) * (1 + pow(math.sin(z),2)/(pow(x+y,1/2)))
	down = pow(math.e, abs(x-y)) + x/2
	two = pow(math.cos(y),3) * up / down
	answer = one + two
	return answer

x = 6.251
y = 0.827
z = 25.001
print(four(x,y,z))
