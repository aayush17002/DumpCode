box=input().split()
box.sort()
players=int(input())
d={}
alpha=[]
for i in box:
	alpha.append(ord(i))
q=min(alpha)
for i in range(players):
	play=input().split()
	p={play[0]:play[1]}
	d.update(p)
count={}
for i in d:
	c=0
	for j in box:
		if d[i]==j:
			c+=1
	a={i:c}
	count.update(a)	
score={}
for i in d:
	s=(ord(d[i])-q)*count[i]
	s1={i:s}
	score.update(s1)
v=max(list(map(int,list(score.values()))))
ap=[]
for i in list(score.keys()):
	if score[i]==v:
		ap.append(i)
ap.sort()
print(ap[0])