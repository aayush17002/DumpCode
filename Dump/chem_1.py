f=input()
l=len(f)
ans=0
for i in range(l):
	for a1 in range(2,51):
		if ((f[i]+f[i+1])==(')'+str(a1))):
			print(a1)
			print(i)
			a=f.rfind('(',i)
			f+=(f[a+1:i])*(a1-1)
				
		else:
			pass
print(f)
l1=len(f)
for i in range(l1):
	for a2 in range(2,51):
		if (f[i]==str(a2)):
			if f[i-1]=='O':
				f+='O'*(a2-1)
			elif f[i-1]=='C':
				f+='C'*(a2-1)
			elif f[i-1]=='H':
				f+='H'*(a2-1)
		else:
			pass
l2=(len(f))
for i in range(l2):
	if f[i]=='O':
		ans+=16
		pass
	elif f[i]=='C':
		ans+=12
		pass
	elif f[i]=='H':
		ans+=1
		pass
	else:
		pass
print(ans)