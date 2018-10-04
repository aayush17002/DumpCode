t = int(input())
for i in range(t):
	N,a,b = map(int,input().split())
	A = list(map(int,input().split()))
	x = [0]*(N+1)
	for i in A:
		x[i] = x[i] + 1
	val = (x[a]*x[b])/(N*N)
	print("%.10f" % val)