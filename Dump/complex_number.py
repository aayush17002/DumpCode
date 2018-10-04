class complex:
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def __str__(self):
		return str(self.a) + '+' + str(self.b) + 'i'
print(complex(3,5)) 