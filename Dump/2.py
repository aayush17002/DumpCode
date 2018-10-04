from random import randint as randi
from random import uniform as randu

N = 100000 
count=0
for k in range(N):
	x = randu(0,100)
	if 10<=x<=20 or 45<=x<=70:
		count +=1
print (float(count)/float(N))

count=0
for k in range(N):
	x = randu(0,100)
	if 10<=x<=45 and 20<=x<=60: 
		count +=1
print (float(count)/float(N))

count=0
for	k in range(N): 
	x = randi(1,20) 
	if x%3==1 or x%5==0:
		count +=1
print (float(count)/float(N))

count=0
for	k in range(N): 
	x = randi(1,20) 
	if 13<=x<17:
		count +=1
print (float(count)/float(N))

