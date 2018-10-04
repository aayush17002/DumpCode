s1=input()
for i in s1:
	x='f_'+str(i)
	globals()[x]=False
for i in globals():
	print(i)
s=input()
l=len(s)
def ish(s,l):
	globals()
	for i in s1:
		if s[0]==str(i):
			x='f_'+str(i)
			globals()[x]=True
	s=s[1:]
	l=len(s)
	print(s)
	if l>0:
		return ish(s,l)
	else:
		return
ish(s,l)
print(f_a)