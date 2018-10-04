import math
def highestpowof2(n):
	p = int(math.log(n,2))
	return p
def expo(a,b):
	result = 1
	while(b>0):
		if(b%2==1):
			result *= a
		b //= 2
		a *= a
	return result
def middle(n):
	x = highestpowof2(n)
	lower = expo(2,x)
	higher = expo(2,x+1)
	# print(lower)
	# print(higher)
	result = [int(math.fabs(n-lower)),int(math.fabs(n-higher))]
	return result

T = int(input())
for i in range(T):
	n = int(input())
	d = middle(n)
	print(d)
	if(n==1):
		print(2)
	elif(d[0]==0):
		print(1)
	else:
		f = middle(d[0])+middle(d[1])
		# print(f)
		print(f)