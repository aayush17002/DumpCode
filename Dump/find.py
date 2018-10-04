global A
def find(x,y):
	global A
	if x>y:
		return 1
	ans=A[x-1]**find(x+1,y)
	return ans

l=int(input())
a=input().split(" ")
for i in range(0,len(a)):
	a[i]=int(a[i])
A=a
t=int(input())
for j in range(0,t):
	q=input().split(" ")
	for k in range(0,len(q)):
		q[k]=int(q[k])
	ans = (find(q[0],q[1]))%2
	if ans==1:
		print("Odd")
	else:
		print("Even")