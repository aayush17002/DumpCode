from math import sqrt as s
x=0
y=1
z=0
while z<1000000:
	z=x+y
	x=y
	y=z
	print(y/x)
print(z)
print((1+s(5))/2)