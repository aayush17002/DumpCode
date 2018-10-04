s=input()
import string
alpha=(string.ascii_letters)+(string.digits)+(string.punctuation)
a=0
p=''
for i in alpha:
	p+='co'+i+'e '
p=p.split()
for x in p:
	a+=s.count(x)
print(a)