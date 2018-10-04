f_e=False
f_l=False
f_f=False
def elfish(s,l):
	global f_e,f_l,f_f
	if s[0]=="e":
		f_e=True
	if s[0]=="l":
		f_l=True
	if s[0]=="f":
		f_f=True
	s=s[1:]
	l=len(s)
	if l>0:
		return elfish(s,l)
	else:
		return
s=input()
l=len(s)
elfish(s,l)
if f_f and f_l and f_e:
	print(True)
else:
	print(False)