import math
def expo(a,b):
	result = 1
	while(b>0):
		if((b&1)==1):
			result *= a
		b =b>>1
		a *= a
	return result
def expo1(a,b,t):
	result = 1
	while(b>0):
		if((b&1)==1):
			result = result*a%t
		b =b>>1
		a = a*a%t
	return result

T = int(input())
for _ in range(T):
	a,b,n = map(int,input().split())
	if(a==b):
		r = 2*expo(a,n)%1000000007
		print(r)
	else:
		t = a-b
		r = expo1(a,n,t)+expo1(b,n,t)
		x = (math.gcd((a-b),r))%1000000007
		print(x)