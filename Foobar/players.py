t=input().split()
coins=int(t[0])
player1=False
player2=False
count=0
def coin_game(coin,p):
	global player1,player2,count
	if coin==1 or coin==2:
		count+=1
		if p==1:
			player1=True
			return
		elif p==2:
			player2=True
			return
	elif coin==4:
		count+=3
		if p==1:
			player1=True
			return
		elif p==2:
			player2=True
			return
	elif coin==3:
		count+=2
		if p==1:
			player2=True
			return
		elif p==2:
			player1=True
			return
	else:
		a=abs((coin%8)-4)
		count+=a
		coin-=4
		if p==1:
			p=2
		elif p==2:
			p=1
		coin_game(coin,p)
coin_game(coins,1)
if player1:
	print(t[1],count)
else:
	print(t[2],count)		
