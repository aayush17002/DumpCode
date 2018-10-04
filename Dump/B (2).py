def printPrevSmaller(arr, n):
	r = []
	for i in range(n):
		while(len(r)!=0 and r[-1]>arr[i]):
			r.pop()
		if(len(r)==0):
			print(arr[i],end=" ")
		else:
			print(r[-1],end=" ")
		r.append(arr[i])
n = int(input())
arr = list(map(int, input().split()))
printPrevSmaller(arr,n)