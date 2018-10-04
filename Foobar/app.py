box=input().split()
box.sort()
players=int(input())
d=[]
c1=[]
alpha=[]
for i in box:
	alpha.append(ord(i))
q=min(alpha)
for i in range(players):
	play=input().split()
	d.append(play[0])
	c1.append(play[1])
score=[]
for i in c1:
	s=(ord(i)-q)*(box.count(i))
	score.append(s)
v=max(score)
g=score.index(v)
print(d[g])