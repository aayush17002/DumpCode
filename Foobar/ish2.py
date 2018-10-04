s1=input()
index={}
for i in s1:
	x={i:False}
	index.update(x)
# print(index)
s=input()
l=len(s)
def ish(s,l):
	global index
	for i in list(index.keys()):
		if s[0]==str(i):
			index[i]=True
	s=s[1:]
	l=len(s)
	# print(s)
	if l>0:
		return ish(s,l)
	else:
		return
ish(s,l)
for i in list(index.values()):
	if not i:
		print(False)
		break
else:
	print(True)
