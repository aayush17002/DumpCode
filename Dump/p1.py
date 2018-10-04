import math
n,k = map(int,input().split())
sqn = int(math.sqrt(n))
divisors = []
for i in range(1,sqn+1):
	if(n%i==0):
		divisors.append(i)
		if(i!=n//i):
			divisors.append(n//i)
divisors.sort()
# print(divisors)
if(len(divisors)<k):
	print(-1)
else:
	print(divisors[k-1])