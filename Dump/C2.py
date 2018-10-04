n,m = map(int,input().split())
if(n==1):
	print(m)
elif(n==2):
	print(m*m%1000000007)
else:
	one = [0 for _ in range(n-1)]
	mm = [0 for _ in range(n-1)]
	one[0] = 1
	mm[0] = m-1
	for i in range(1,n-1):
		one[i] = mm[i-1]
		mm[i] = (m-1)*(one[i-1]%1000000007+one[i]%1000000007)%1000000007
	result = m*(mm[n-2]%1000000007+mm[n-3]%1000000007)%1000000007
	result %= 1000000007
	print(one)
	print(mm)
	print(result)