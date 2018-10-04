num=input().split()
num=list(map(int,num))
a=num[0]
b=num[1]
c=num[2]
x1=abs(a-b)
x2=abs(a-c)
x3=abs(b-c)
if x1<=1:
	if x2>=2 and x3>=2:
		print(True)
	else:
		print(False)
elif x2<=1:
	if x1>=2 and x3>=2:
		print(True)
	else:
		print(False)
else:
	print(False)