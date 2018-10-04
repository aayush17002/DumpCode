x=list(map(int,input().split()))
a=x[0]
b=x[1]
w=b-a
t=1
if b<a:
	print(0)
elif b==a:
	print(1)
elif w>=10:
	print(0)
else:
	for i in range(a+1,b+1):
		t*=i
	t=t%10
	print(int(t))