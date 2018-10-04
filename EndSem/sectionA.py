from copy import *
class Myset:
	def __init__(self,S):
		self.S=S
		self.c=deepcopy(S)
		for i in range(0,len(self.S)-1):
			for j in range(len(self.S),i,-1):
				if self.S[i]==self.S[j]:
					self.S.pop(j)
	def __str__(self):
		return self.S

print(Myset([4,5,6,5,5]))