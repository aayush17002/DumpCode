s=input("enter a string:")
t=s[0]
for x in s:
	flag=False
	for y in t:
		if x == y:
			flag=True
	if not flag:
		t=t+x			
print(t)			