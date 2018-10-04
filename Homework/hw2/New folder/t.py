import random
tile=[0 for i in range(9)]
def validmove(move):
	global tile
	if tile[move]==0:
		return True
	else:
		return False

def win():
	global tile
	if ((tile[0] == 1 and tile[1] == 1 and tile[2] == 1) or (tile[3] == 1 and tile[4] == 1 and tile[5] == 1) or (tile[6] == 1 and tile[7] == 1 and tile[8] == 1) or (tile[0] == 1 and tile[3] == 1 and tile[6] == 1) or (tile[1] == 1 and tile[4] == 1 and tile[7] == 1) or (tile[2] == 1 and tile[5] == 1 and tile[8] == 1) or (tile[2] == 1 and tile[4] == 1 and tile[6] == 1) or (tile[0] == 1 and tile[4] == 1 and tile[8] == 1)):
		return 1
	elif ((tile[0] == 2 and tile[1] == 2 and tile[2] == 2) or (tile[3] == 2 and tile[4] == 2 and tile[5] == 2) or (tile[6] == 2 and tile[7] == 2 and tile[8] == 2) or (tile[0] == 2 and tile[3] == 2 and tile[6] == 2) or (tile[1] == 2 and tile[4] == 2 and tile[7] == 2) or (tile[2] == 2 and tile[5] == 2 and tile[8] == 2) or (tile[2] == 2 and tile[4] == 2 and tile[6] == 2) or (tile[0] == 2 and tile[4] == 2 and tile[8] == 2)):
		return 2	
	else:
		return 0
def takeNaiveMove(play):
	num=random.randint(0,8)
	global tile
	if validmove(num)==True:
		tile[num]=play
	else:
		takeNaiveMove(play)
print(takeNaiveMove(1))
print(takeNaiveMove(2))
print(takeNaiveMove(3))
print(takeNaiveMove(4))
print(takeNaiveMove(5))
print(takeNaiveMove(6))

def takeStrategicMove(play):
	if tile[4]==0:
		tile[4]=play
	else:
		if tile[0]==0:
			tile[0]=play
		elif tile[2]==0:
			tile[2]=play
		elif tile[6]==0:
			tile[6]=play
		elif tile[8]==0:
			tile[8]=play
		else:
			if tile[1]==0:
				tile[1]=play
			elif tile[3]==0:
				tile[3]=play
			elif tile[5]==0:
				tile[5]=play
			elif tile[7]==0:
				tile[7]=play
	
def validBoard(naive=2):
	global tile
	if naive==1:
		if win()==0:
			for i in range(9):
				if tile[i]!=0:
					return True
			else:
				return False
		else:
			return False
	elif naive==2:
		if win()==0:
			if ((tile[0]!=0 and tile[7]!=0 and tile[2]!=0)or
				(tile[2]!=0 and tile[3]!=0 and tile[8]!=0)or
				(tile[8]!=0 and tile[1]!=0 and tile[6]!=0)or
				(tile[0]!=0 and tile[5]!=0 and tile[6]!=0)):
				return False
			else:
				for i in range(9):
					if tile[i]!=0:
						return True
				else:
					return False
		else:
			return False

def game(gametype=1):
	if gametype==1:
		tile=[0 for i in range(9)]
		while validBoard(1)==True:
			takeNaiveMove(1)
			takeNaiveMove(2)
		return win()
	elif gametype==2:
		while validBoard()==True:
			takeNaiveMove(1)
			takeStrategicMove(2)
		return win()
	elif gametype==3:
		while validBoard()==True:
			takeStrategicMove(1)
			takeStrategicMove(2)
		return win()

def game1(n=10):
	count=0
	for i in range(n):
		# tile=[0 for i in range(9)]
		if game(1)==1:
			count+=1
	return (count/n)

def game2(n=10):
	count=0
	for i in range(n):
		# tile=[0 for i in range(9)]
		if game(2)==1:
			count+=1
	return (count/n)

def game3(n=10):
	count=0
	for i in range(n):
		# tile=[0 for i in range(9)]
		if game(3)==1:
			count+=1
	return (count/n)
print(game1(1))