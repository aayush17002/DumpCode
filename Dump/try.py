import numpy as np
p,s = map(int,input().split())
A = [0 for _ in range(p)]
for i in range(p):
	sc = [0 for t in range(100)]
	x = list(map(int,input().split()))
	y = list(map(int,input().split()))
	for j in range(len(y)):
		sc[x[j]-1] = y[j]
	j=0
	while(j<100):
		if(sc[j]!=0):
			k = j+1
			if(k<100):
				print(k)
				while(k<100 or sc[k]==0):
					k += 1
					if(k==100):
						break
			if(k>=100):
				break
			if(sc[j]>sc[k]):
				A[i] += 1
			j = k-1
		j += 1
		if(j==100):
			break
print(A)
ans = np.array(A)
i = np.argsort(ans)
for j in range(p):
	print(i[j]+1)