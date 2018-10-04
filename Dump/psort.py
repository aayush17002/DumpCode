p,s = map(int,input().split())
A = [[0,_] for _ in range(p)]
for i in range(p):
	x = list(map(int,input().split()))
	y = list(map(int,input().split()))
	finalA = [[0,0] for _ in range(s)]
	for j in range(s):
		finalA[j][0] = x[j]
		finalA[j][1] = y[j]
	finalA.sort()
	for j in range(s-1):
		if(finalA[j][1]>finalA[j+1][1]):
			A[i][0] += 1
A.sort()
for j in range(p):
	print(A[j][1]+1)