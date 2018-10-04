def countSetBits(n):
	if(n==0):
		return 0
	else:
		return 1+countSetBits(n&(n-1))

def snoob(x):
	next1 = 0;
	if(x>0):
		rightOne = x & (~x+1)
		nextHigherOneBit = x + rightOne
		rightOnesPattern = x ^ nextHigherOneBit
		rightOnesPattern //= rightOne
		rightOnesPattern >>= 2
		next1 = nextHigherOneBit | rightOnesPattern
	return next1

def replace_str_index(text,index=0,replacement=''):
	if(index==-1):
		return '%s%s'%(text[:index],replacement)
	else:
		return '%s%s%s'%(text[:index],replacement,text[index+1:])

n,k = map(int,input().split())
val = countSetBits(n)
if(val==k):
	print(snoob(n))
elif(val<k):
	diff = k-val
	x = bin(n)[2:]
	z = "00000000000000000000000000000000000000000000000000000000000000"
	x = z+x
	l = 1
	while (diff>0):
		if(x[-l]=="0"):
			x = replace_str_index(x,-l,'1')
			diff -= 1
		l += 1
	n = int(x,2)
	print(n)
else:
	x = bin(n)[2:]
	count = 0
	i = 0
	while(count<k):
		if(x[i]=="1"):
			count += 1
		i += 1
	for j in range(i,len(x)):
		x = replace_str_index(x,j,'0')
	n = int(x,2)
	print(snoob(n))