import random
def sT(nF):
	prev=random.randint(0,1)
	for i in range (1,nF):
		curr=random.randint(0,1)
		if curr==prev==1:
			return True
		prev=curr
	return False
def sim():
	p=0
	for i in range(10000):
		if sT(5):
			p+=1
	return (p/10000)
print(sim())
