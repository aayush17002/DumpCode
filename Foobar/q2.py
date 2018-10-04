class nonTA:
	def __init__(self,ta,nonta,upgrade):
		self.result=""
		self.ta=ta
		self.nonta=nonta
		self.upgrade=upgrade
		self.count1=0
		self.marks=[]
		for i in range(len(self.ta)):
			if self.count1<((len(self.ta)//2)+1):
				if int(self.ta[i])<int(self.nonta[i]):
					self.count1+=1
				else:
					diff=int(self.ta[i])-int(self.nonta[i])+1
					x=int(self.upgrade[i])*diff
					self.marks.append(x)
			else:
				break
		self.marks.sort()
		if self.count1<((len(self.ta)//2)+1):
			dif=(len(self.ta)//2)+1-self.count1
			x1=0
			for i in range(dif):
				x1+=self.marks[i]
			self.result=str(x1)
		else:
			self.result="0"
	def __str__(self):
		return self.result
if __name__=="__main__":
	T=int(input())
	for i in range(T):
		players=int(input())
		plist=input().split()
		upgrade=input().split()
		pTA=[]
		pnonTA=[]
		for i in range(players):
			pTA.append(plist[i])
		for i in range(players,len(plist)):
			pnonTA.append(plist[i])

		p1=nonTA(pTA,pnonTA,upgrade)
		print(p1)