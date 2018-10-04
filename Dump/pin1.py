from math import ceil
t=int(input())
q=""
m0=(10**9)+7
for i in range(t):
	side=input().split()
	m=int(side[0])
	n=int(side[1])
	N=int(input())
	for a in range(N):
		k=int(input())
		m1=ceil(m/k)
		n1=ceil(n/k)
		p=str((m1*n1)%m0)
		q=q+(p)+"\n"
print(q)		