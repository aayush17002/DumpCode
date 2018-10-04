import math
n,p = map(int,input().split())
A = list(map(int,input().split()))
length = 0
if(A[0]>=p):
	length = 1
else:
	length = 0
maxlength = 0
temp = A[0]
for i in range(1,n):
	temp = math.gcd(temp,A[i])
	if(temp>=p):
		length += 1
	else:
		temp = A[i]
		if(maxlength<length):
			maxlength = length
		if(A[i]>=p):
			length = 1
		else:
			length = 0
if(maxlength<length):
	maxlength = length
else:
	maxlength = maxlength
print(maxlength)