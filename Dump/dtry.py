n,h = map(int,input().split())
A = list(map(int,input().split()))
maxi = 0
for i in A:
	if(maxi<i):
		maxi = i
if(n==h):
	print(maxi)
else:
	low = 1
	high = maxi
	sumi = 0
	ans = 0
	while(low<=high):
		mid = (high+low)//2
		sumi = 0
		for i in range(n):
			sumi = sumi + (A[i]//mid)
			if(A[i]%mid!=0):
				sumi += 1
		if(sumi>h):
			low = mid+1
		else:
			high = mid-1
			ans = mid
	print(ans)