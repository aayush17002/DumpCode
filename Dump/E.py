def solver(i,sites,arr):
	length = 1
	index = arr[i]
	sites[i] = True
	while(index!=i):
		sites[index] = True
		length += 1
		index = arr[index]
	return (length,sites)
n = int(input())
arr = list(map(int,input().split()))
arr = [0] + arr
sites = [False for _ in range(n+1)]
groupslength = []
for i in range(1,n+1):
	if(sites[i]==False):
		a,sites = solver(i,sites,arr)
		groupslength.append(a)
groupslength.sort()
if(len(groupslength)==1):
	print(groupslength[0]**2)
else:
	ans = 2*groupslength[-1]*groupslength[-2]
	for i in groupslength:
		ans += i*i
	print(ans)