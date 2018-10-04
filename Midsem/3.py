T=int(input())
n=int(input())
def 
for i in range(T):
	e=0
	L=int(input())
	num=input().split()
	num=list(map(int,num))
	if len(num)==L:
		for t in num:
			if t%n==0:
				e+=1
	if e!=0:
		print(True)
	else:
		print(False)
