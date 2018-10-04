t=input().split()
coins=int(t[0])
count_p1=0
count_p2=0
combinations=[]
def s1(coins,level):
	global combinations
	if level==1:

		t=[]
		for i in range(coins):
			t.append(1)
		combinations.append(t)
		