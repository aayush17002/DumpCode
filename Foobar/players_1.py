coins=int(input("enter the number of coins "))
player1=False
player2=False
def coin_game(coin,p):
	global player1,player2
	if coin==1 or coin==2 or coin==4 or coin==8 or coin==5 or coin==7:
		if p==1:
			player1=True
			return
		elif p==2:
			player2=True
			return
	elif coin==3 or coin==6:
		if p==1:
			player2=True
			return
		elif p==2:
			player1=True
			return
	else:
		if p==1:
			p=2
		elif p==2:
			p=1
		coin-=4
		coin_game(coin,p)
coin_game(coins,1)
if player1:
	print("player1")
else:
	print("player2")		
