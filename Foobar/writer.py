a=input().split()
s=input()
# t=[]
for i in range(int(a[1])):
	x=input().split()
	if x[0]=="T" or x[0]=="t":
		s+=str(x[1])
	elif x[0]=="C" or x[0]=="c":
		# t.append(len(s))
		print(len(s))
	elif x[0]=="W" or x[0]=="w":
		p=len(s)-int(x[1])
		s=s[:p]
# for i in t:
# 	print(i)