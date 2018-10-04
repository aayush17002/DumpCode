def calculater(mid,arr):
	result = 0
	for i in arr:
		if(i%mid==0):
			result += i//mid
		else:
			result += 1+(i//mid)
	return result
def binarySearch(l,r,h,arr):
	while(l<r):
		mid = (l+r)//2
		x = calculater(mid,arr)
		print(mid)
		print(x)
		if(x==h):
			return mid
		elif(x<h):
			l = mid
		else:
			r = mid
	return l
n,h = map(int,input().split())
arr = list(map(int,input().split()))
l = min(arr)
r = max(arr)
print(arr)
print(binarySearch(l,r,h,arr))