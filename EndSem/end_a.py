from copy import *
class Myset:
	def __init__(self, S):
		self.S = S
		self.S.sort()
		self.L=[]
		for i in self.S:
			if i not in self.L:
				self.L.append(i)
	def __add__(self,other):
		if type(other)==Myset:
			self.l=deepcopy(self.L)
			self.l.extend(other.L)
			return Myset(self.l)
		else:
			self.l=deepcopy(self.L)
			self.l.append(other)
			return Myset(self.l)
	def __radd__(self,other):
		self.l=deepcopy(self.L)
		self.l.append(other)
		return Myset(self.l)
	def __str__(self):
		return str(self.L)
if __name__ == '__main__':
	s1=Myset([4,5,6,5,5])
	print(s1)
	s2=Myset([2,3,4,5,6,7])
	print(s2)
	s3=s1+s2
	print(s3)
	s4=s1+23
	print(s4)
	s5=23+s1
	print(s5)