T=int(input())
for i in range(T):
	S=input()
	l=len(S)-1
	for a in range(0,l):
		if S[a]==S[a+1]:
			p="YES"
			break
		else:
			p="NO"
	print(p)		