def mul(a,b):
	if a==0 or b==0:
		return 0
	elif b>0:
		return (a+mul(a,b-1))
	elif b<0:
		return (-mul(a,-b))
print(mul(int(input()),int(input())))