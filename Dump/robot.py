x = 0 
y = 0 
T =""

for i in range(2000) :
	if abs(x) < L-1 and abs(y) < L-1:
		# The robot has not reached the edge
		r = randi(1,4)
		if r==1:
			# Hop North
			y = y + 2; T = T + 'NN' 
		elif r==2:
			# Hop East
			x = x + 2; T = T + 'EE' 
		elif r==3:
			# Hop South
			y = y-2; T = T + 'SS' 
		else:
			# Hop West
			x = x-2; T = T + 'WW'
	else:
		break
