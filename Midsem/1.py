def R(n3,n):
	i1=''
	for i in range(n3+1):
		for t in range(n3+1):
			if n==(i**3)+(t**3) and i!=t:
				i1+='('+str(i)+' '+str(t)+')'
	if i1!='' and i1.count(')')==4:
		return n
	else:
		return
num=int(input())
for x in range(num):
	n=x
	n3=int(n**(1/3))
	a=R(n3,n)
	if a!=None:
		print(a)