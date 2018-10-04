T=int(input())


for i in range(T):
	N=int(input())
	for a in range(N):
		p=''
		Pin=(input().split())
		for t in range (len(Pin)):
			if (Pin[t]=='110020' or Pin[t]=='110021'):
				p+=('Okhla ')
				pass
			elif (Pin[t]=='110055' or Pin[t]=='110056'):
				p+=('Rohini ')
				pass
			elif (Pin[t]=='110075'):
				p+=('Dwarka ')
				pass
			else:
				p+=('Others ')
				pass
			
		print(p)
		break