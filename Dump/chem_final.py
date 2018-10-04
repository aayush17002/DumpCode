f=input()
l=len(f)
ans=0
for i in range(l):
	if (f[i]=='2'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=f[a+1:i-1]
			
		elif f[i-1]=='O':
			f+='O'
			
		elif f[i-1]=='C':
			f+='C'
			
		elif f[i-1]=='H':
			f+='H'
			
	elif (f[i]=='3'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*2
			
		elif f[i-1]=='O':
			f+='O'*2
			
		elif f[i-1]=='C':
			f+='C'*2
			
		elif f[i-1]=='H':
			f+='H'*2
			
	elif (f[i]=='4'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*3
			
		elif f[i-1]=='O':
			f+='O'*3
			
		elif f[i-1]=='C':
			f+='C'*3
			
		elif f[i-1]=='H':
			f+='H'*3
			
	elif (f[i]=='5'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*4
		
		elif f[i-1]=='O':
			f+='O'*4
			
		elif f[i-1]=='C':
			f+='C'*4
			
		elif f[i-1]=='H':
			f+='H'*4
			
	elif (f[i]=='6'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*5
			
		elif f[i-1]=='O':
			f+='O'*5
			
		elif f[i-1]=='C':
			f+='C'*5
			
		elif f[i-1]=='H':
			f+='H'*5
			
	elif (f[i]=='7'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*6
			
		elif f[i-1]=='O':
			f+='O'*6
			
		elif f[i-1]=='C':
			f+='C'*6
			
		elif f[i-1]=='H':
			f+='H'*6
			
	elif (f[i]=='8'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*7
		elif f[i-1]=='O':
			f+='O'*7
		elif f[i-1]=='C':
			f+='C'*7
		elif f[i-1]=='H':
			f+='H'*7
	elif (f[i]=='9'):
		if f[i-1]==')':
			a=f.rfind('(')
			f+=(f[a+1:i-1])*8
		elif f[i-1]=='O':
			f+='O'*8
		elif f[i-1]=='C':
			f+='C'*8
		elif f[i-1]=='H':
			f+='H'*8
	else:
		pass
print(f)
l1=(len(f))
for i in range(l1):
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
