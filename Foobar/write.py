def dist(a,b):
	return abs(int(a)-int(b))
def check(s,d):
	min_p=s[0]
	t=0
	for i in s.keys():
		if s[i]<min_p:
			min_p=s[i]
			t=i
	return min_p

T=int(input())
for i in range(T):
	n=int(input())
	d=input().split()
	l={}
	for j in range(len(d)):
		x=[]
		for t in range(len(d)):
			a=dist(d[j],d[t])
			x.append(a)
		s=sum(x)
		l[j]=s
	print(check(l,d))
