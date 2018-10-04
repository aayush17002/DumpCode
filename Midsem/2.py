a1=input().split()
N=int(a1[0])
Q=int(a1[1])
ar=[[] for t in range(N)]
for i in range(N):
	a2=input().split()
	for p in a2:
		ar[i].append(int(p))
	ar[i].sort()
	if len(a2)==5:
		print(ar[i])

"""for t in range(Q):
	a3=input.split()
	if len(a3)==3:"""
