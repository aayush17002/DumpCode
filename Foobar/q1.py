class palindrome:
	def __init__(self,s):
		self.s=s
		l=len(s)-1
		self.s=list(self.s)
		if l%2==0:
			for i in range(l//2):
				self.s[l//2]="a"
				if self.s[i]!="." and self.s[l-i]!=".":
					if self.s[i]!=self.s[l-i]:
						self.s=["-1"]
						break
				elif self.s[i]=="." and self.s[l-i]!=".":
					self.s[i]=self.s[l-i]
					#s.replace('.',str(s[l-i]))
				elif self.s[l-i]=="." and self.s[i]!=".":
					self.s[l-i]=self.s[i]
				else:
					self.s[l-i]=self.s[i]="a"
		else:
			for i in range((l//2)+1):
				if self.s[i]!="." and self.s[l-i]!=".":
					if self.s[i]!=self.s[l-i]:
						self.s=["-1"]
						break
				elif self.s[i]=="." and self.s[l-i]!=".":
					self.s[i]=self.s[l-i]
				elif self.s[l-i]=="." and self.s[i]!=".":
					self.s[l-i]=self.s[i]
				else:
					self.s[l-i]=self.s[i]="a"
		if self.s!=["-1"]:
			x=""
			for i in range(l+1):
				x+=(str(self.s[i]))
			self.s=x
		else:
			self.s="-1"
	def __str__(self):
		return self.s
if __name__=="__main__":
	T=int(input())
	for i in range(T):
		a=int(input())
		p1=palindrome(input())
		print(p1)