import math
def maxPrimeFactors (n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1     
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)
T = int(input())
for _ in range(T):
	n = int(input())
	x = maxPrimeFactors(n)
	count = 0
	flag = False
	while (n%x==0):
		n = n//x
		count += 1
		if(count==2):
			flag = True
			break
	if(flag):
		print("YES")
	else:
		print("NO")
