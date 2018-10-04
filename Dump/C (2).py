def solver(m,level,now):
	if(level==0):
		if(now==-1):
			return 1
		else:
			return (m-1)
	else:
		if(now==-1):
			return solver(m,level-1,(m-1))%1000000007
		else:
			return ((m-1)*((solver(m,level-1,(m-1))%1000000007)+(solver(m,level-1,-1)%1000000007)))%1000000007
		
n,m = map(int,input().split())
if(n==1):
	print(m)
else:
	result = m*((solver(m,n-2,-1)%1000000007)+(solver(m,n-2,(m-1))%1000000007))%1000000007
	result %= 1000000007
	print(result)
