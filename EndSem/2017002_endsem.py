'''Name: Aayush Gupta
Roll Number: 2017002'''
from copy import *
class Multiset(object):
	"""docstring for Multiset"""
	def __init__(self, elements):
		self.data = elements
		self.data.sort()
	def __mul__(self,other):
		self.l=[]
		if other>1:
			for i in self.data:
				for j in range(other):
					self.l.append(i)
		elif other==1:
			self.l=self.data
		elif other==0:
			pass
		return Multiset(self.l)
	def __sub__(self,other):
		self.l1=deepcopy(self.data)
		self.l2=deepcopy(other.data)
		for i in self.l2:
			if i in self.l1:
				self.l1.remove(i)
		return Multiset(self.l1)
	def subset(self,other):
		if self.data==other.data:
			return True
		else:
			self.l1=deepcopy(other.data)
			self.l2=deepcopy(self.data)
			for i in self.l2:
				if i in self.l1:
					self.l1.remove(i)
				else:
					return False
		return True
	def __str__(self):
		return str(self.data)
if __name__ == '__main__':
	M1=Multiset([1,1,2,3,4,4,5])
	M2=Multiset([1,2,3])
	K=2
	M3=M1*K
	M4=M2*3
	M5=M1*0
	M6=M5*8
	print('M1='+ str(M1))
	print('M2='+ str(M2))
	print('M3= M1 * 2 :'+ str(M3))
	print('M4= M2 * 3 :'+ str(M4))
	print('M5= M1 * 0 :'+ str(M5))
	print('M6= M5 * 8 :'+ str(M6))
	M7=M3-M4
	M8=M7-M6
	M9=M8-M3
	print('M3='+ str(M3))
	print('M4='+ str(M4))
	print('M7= M3 - M4 :'+ str(M7))
	print('M8= M7 - M6 :'+ str(M8))
	print('M9= M8 - M3 :'+ str(M9))
	t=M8.subset(M3)
	t=M3.subset(M8)
	t=M9.subset(M8)
	t=M9.subset(M9)
	print('M3='+ str(M3))
	print('M8='+ str(M8))
	print('M9='+ str(M9))
	print('M8.subset(M3) :'+ str(M8.subset(M3)))
	print('M3.subset(M8) :'+ str(M3.subset(M8)))
	print('M9.subset(M8) :'+ str(M9.subset(M8)))
	print('M9.subset(M9) :'+ str(M9.subset(M9)))