def f(n1,n2):
	d=()
	for i in range(1,min(n1,n2)+1):
		if n1%i==0 and n2%i==0:
			d+=(i,)
	return d
a=int(input())
b=int(input())
d=f(a,b)
print(d)
t=0
for al in d:
	t+=al
print(t)