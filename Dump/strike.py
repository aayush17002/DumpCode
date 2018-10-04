T = int(input())
for i in range(T):
	N = int(input())
	p = 1
	q = 0
	if(N==1):
		q = 1
	else:
		a = (N//2)+(N%2)
		q = 10**(N-a)
	print(p,end=" ")
	print(q)