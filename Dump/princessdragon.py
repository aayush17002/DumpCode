def calans(arr,i,p,n):
	arru = []
	if(i!=0 or i!=(n-1)):
		arru = arr[0:i]+arr[i+1:]
	elif(i==0):
		arru = arr[1:]
	else:
		arru = arr[:-1]
	arru.sort(reverse=True)
	r = 0
	for i in arru:
		if(p>0):
			p -= i
			r += 1
		else:
			break
	if(p>0):
		return n
	return r
T = int(input())
for _ in range(T):
	n,p = map(int, input().split())
	ans = [0 for x in range(n)]
	arr = list(map(int,input().split()))
	for i in range(n):
		pp = p-arr[i]
		ans[i] = n - calans(arr,i,pp,n)
	for i in ans:
		print(i,end=" ")