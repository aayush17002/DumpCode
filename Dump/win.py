stick=input().split()
p=int(stick[0])
k=int(stick[1])
while p>(2*k):
	p-=(2*k)
if (k<=p<(2*k)):
	print("YES")
	pass
elif (p==(2*k) or p<k):
	print("NO")
	pass