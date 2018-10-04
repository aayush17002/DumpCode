T = int(input())
for _ in range(T):
	n = int(input())
	A = list(map(int, input().split()))
	A.sort()
	mini = A[1]-A[0];
	for i in range(1,n-1):
		c = A[i+1]-A[i]
		if(c<mini):
			mini = c
	print(mini)