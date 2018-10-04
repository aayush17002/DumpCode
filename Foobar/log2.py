import math                                                                                                         
def log2(n): 
	return math.log(n,2)                                                                                                                    
def f(n):  
	if n<1:                                                                
		return 'ihihbuv'    
	c=int(log2(n))                                                                                            
	ans='n= '        
	for j in range(c): 
		if n%(2**c)<n:
			ans=ans+'1'
			n=n-2**c
		else:
			ans=ans+'0'
	return ans
for i in range(7):
	print(f(i))