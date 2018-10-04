g={0:[],1:[0,2,3,4],2:[3,4],3:[1,2],4:[0]}
h={}
for x in g:
	v=g[x]
	for node in v:
		if node in h:
			h[node].append(x)
		else:
			h[node]=[x]
print(h)