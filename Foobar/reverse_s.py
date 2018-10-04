def reverse_s(l,lenght):
	if lenght>1:
		x=[]
		for i in range(1,lenght):
			x.append(l[i])
		x.append(l[0])
		t=len(l)
		if t!=lenght:
			for i in range(lenght,t):
				x.append(l[i])
		return reverse_s(x,lenght-1)
	else:
		x=""
		for i in l:
			x+=str(i)+" "
		return x
x=input().split()
l=len(x)
print(reverse_s(x,l))