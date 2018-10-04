import math
class point:
	def __init__(self,Xi,Yi):
		self.x=Xi
		self.y=Yi
	def distance(self,other):
		self.x1=abs(self.x-other.x)
		self.y1=abs(self.y-other.y)
		return math.sqrt((self.x1**2)+(self.y1**2))

	def __str__(self):
		return '('+str(self.x)+','+str(self.y)+')'
def checker(Dist,K,R):
	if K==0:
		for c in Dist:
			if c>R:
				return "NO"
		return "Yes"
	else:
		count=0
		for c in Dist:
			if c>R:
				count+=1
		if count>K:
			return "NO"
		else:
			return "Yes"

T=int(input())
for i in range(T):
	N,K,R=input().split()
	N,K,R=int(N),int(K),int(R)
	if R>0:
		L=[]
		Dist=[]
		for j in range(N):
			Xi,Yi=input().split()
			Xi,Yi=int(Xi),int(Yi)
			L.append(point(Xi,Yi))
		for z in range(len(L)):
			for x in range(z,len(L)):
				Dist.append(L[z].distance(L[x]))
		print(checker(Dist,K,R))


	else:
		print("NO")
