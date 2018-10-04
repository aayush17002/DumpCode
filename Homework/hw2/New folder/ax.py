import random 
tile0= 0    
tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
s=[]
def validmove(move):
	global s
	if int(move) in s:
		return False
	else:
		s.append(int(move))
		return True
def win():
	if ((tile0 == 1 and tile1 == 1 and tile2 == 1) or # across the top
		(tile3 == 1 and tile4 == 1 and tile5 == 1) or # across the middle
		(tile6 == 1 and tile7 == 1 and tile8 == 1) or # across the bottom
		(tile0 == 1 and tile3 == 1 and tile6 == 1) or # down the left side
		(tile1 == 1 and tile4 == 1 and tile7 == 1) or # down the middle
		(tile2 == 1 and tile5 == 1 and tile8 == 1) or # down the right side
		(tile2 == 1 and tile4 == 1 and tile6 == 1) or # diagonal
		(tile0 == 1 and tile4 == 1 and tile8 == 1)):# diagonal
		return 1
	elif ((tile0 == 2 and tile1 == 2 and tile2 == 2) or # across the top
		(tile3 == 2 and tile4 == 2 and tile5 == 2) or # across the middle
		(tile6 == 2 and tile7 == 2 and tile8 == 2) or # across the bottom
		(tile0 == 2 and tile3 == 2 and tile6 == 2) or # down the left side
		(tile1 == 2 and tile4 == 2 and tile7 == 2) or # down the middle
		(tile2 == 2 and tile5 == 2 and tile8 == 2) or # down the right side
		(tile2 == 2 and tile4 == 2 and tile6 == 2) or # diagonal
		(tile0 == 2 and tile4 == 2 and tile8 == 2)):# diagonal
		return 2	
	else:
		return 0
	
def takeNaiveMove(player):
	#q=0
	num=random.randint(0,8)
	alpha=[0,1,2,3,4,5,6,7,8]
	while validmove(num)!=True:
		alpha.remove(num)
		num=random.choice(alpha)
	print(num)
		#q+=1
	"""print(q)
	print(num)"""
	x='tile'+str(num)
	globals()[x]=int(player)

def takeStrategicMove(player):
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile0
	if validmove(4)==True:
		tile4=int(player)
	else:
		if validmove(8)==True:
			tile8=int(player)
		elif validmove(6)==True:
			tile6=int(player)
		elif validmove(2)==True:
			tile2=(player)
		elif validmove(0)==True:
			tile0=int(player)
		else:
			if validmove(7)==True:
				tile7=(player)
			elif validmove(5)==True:
				tile5=int(player)
			elif validmove(3)==True:
				tile3=int(player)
			elif validmove(1)==True:
				tile1=int(player)

	
def validBoard(x):
	if win()==0:
		if x==1:
			for i in range(9):
				j='tile'+str(i)
				if globals()[j]==0:
					return True
				else:
					return False
		if x==2:
			global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile0	
			if tile0==0:
				return True
			elif tile1==0:
				return True
			elif tile2==0:
				return True
			elif tile3==0:
				return True
			elif tile4==0:	
				return True
			elif tile5==0:
				return True
			elif tile6==0:	
				return True
			elif tile7==0:
				return True
			elif tile8==0:	
				return True
			else:
				return False
	else:
		return False

def game(gametype=1):
	if gametype==1:
		while validBoard(1)==True:
			takeNaiveMove(1)
			takeNaiveMove(2)
		return win()
	elif gametype==2:
		while validBoard(2)==True:
			takeNaiveMove(1)
			takeStrategicMove(2)
		return win()
	elif gametype==3:
		while validBoard(2)==True:
			takeStrategicMove(1)
			takeStrategicMove(2)
		return win()

def game1(n=10):
	count1=0
	count2=0
	count3=0
	for t in range(n):
		for i in range(9):
			x='tile'+str(i)
			globals()[x]=0
		global s
		s=[]
		if game(1)==1:
			count1+=1
		elif game(1)==2:
			count2+=1
		elif game(1)==0:
			count3+=1
	return (count1/n),(count2/n),(count3/n)

	

def game2(n=10):
	count1=0
	count2=0
	count3=0
	for t in range(n):
		for i in range(9):
			x='tile'+str(i)
			globals()[x]=0
		global s
		s=[]
		if game(2)==1:
			count1+=1
		elif game(2)==2:
			count2+=1
		elif game(2)==0:
			count3+=1
	return (count1/n),(count2/n),(count3/n)

def game3(n=10):
	count1=0
	count2=0
	count3=0
	for t in range(n):
		for i in range(9):
			x='tile'+str(i)
			globals()[x]=0
		global s
		s=[]
		if game(3)==1:
			count1+=1
		elif game(3)==2:
			count2+=1
		elif game(3)==0:
			count3+=1
	return (count1/n),(count2/n),(count3/n)

print(game1())
print(game2())
print(game3())