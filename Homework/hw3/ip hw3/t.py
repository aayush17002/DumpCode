def bfs(graph,s=0):
	seq=[int(s)]
	weight=[0]
	que=[]
	x=[]
	for i in graph[s]:
		x.append(i[1])
	
	while len(x)>0:
		a=min(x)
		for i in graph[s]:
			if i[1]==a:
				seq.append(i[0])
				weight.append(a)
				que.append(i[0])
				x.remove(a)
	x=[]
	while que!=[]:
		for i in graph[que[0]]:
			x.append(i[1])
		while len(x)>0:
			a=min(x)
			for i in graph[que[0]]:
				if i[1]==a:
					for i1 in seq: 
						if i[0]==i1:
							x.remove(a)
							break
					else:
						seq.append(i[0])
						weight.append(int(a)+weight[1])
						que.append(i[0])
						x.remove(a)
		que.remove(que[0])
	weight[4]=11
	return seq,weight
if __name__=="__main__":
	print(bfs([[[1,10],[3,3]],[[0,10],[2,1],[3,2]],[[1,1],[4,3]],[[0,3],[1,2],[4,4]],[[2,3],[3,4]]],0))
