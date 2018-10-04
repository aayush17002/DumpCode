def nw_max(a,l=2):
	if l==1:
		return max(a)
	else:
		l-=1
		x=a.index(max(a))
		a=a[:x]+a[x+1:]
		return nw_max(a,l)
if __name__=="__main__":
	num=int(input("enter the number of terms to be compared "))
	x=[]
	for i in range(num):
		x.append(int(input("enter a number ")))
	n=int(input("enter which max to take out "))
	while (n<=0  and n>len(x)):
		n=int(input("enter which max to take out "))
	print(nw_max(x,n))