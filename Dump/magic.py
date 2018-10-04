s = [0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071,262143,524287,1048575,2097151,4194303,8388607,16777215,33554431,67108863,134217727,268435455,536870911,1073741823]
T = int(input())
for i in range(T):
	n,m = map(int,input().split())
	A = list(map(int,input().split()))
	count = 0
	for j in range(n):
		val = A[j]%m
		if(val==0):
			count = count + 1
	print(s[count])