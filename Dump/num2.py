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

T = int(input())
for i in range(T):
	n = int(input())
	if(n==1):
		print(2)
	else:
		x = highestpowof2(n)
		val1 = expo(2,x+1)+1-n
		mid = expo(2,x)
		d = n-mid
		if(d==0):
			print(1)
		else:
			r = 10000000000
			y = highestpowof2(d)
			val2 = mid+expo(2,y)
			if((y+1)<x):
				val3 = mid+expo(2,y+1)
				r = min(int(math.fabs(n-val2)),int(math.fabs(n-val3)))
			else:
				r = int(math.fabs(n-val2))
			print(min(val1,r))