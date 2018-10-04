import copy
def lis(p):
	d=[[] for i in range(p)]
	for i in range(p):
		con=int(input())
		for t in range(con):
			x=input().split()
			x=[int(x[0]),int(x[1])]
			d[i].append(x)

	for i in range(1,len(d)):
		if len(d[i])>0:	
			for j in range(len(d)):
				if j!=i:
					for t in range(len(d[i])):
						if d[i][t][0]!=j:
							for z in range(len(d[j])):
								if d[j][z][0]==i:
									x=[j,d[j][z][1]]
									d[i].append(x)
									break
							break
		else:
			for j in range(len(d)):
				if j!=i:
					for t in range(len(d[j])):
						if t!=i:
							if d[j][t][0]==i:
								x=[j,d[j][t][1]]
								d[i].append(x)
								break
	return d
def bfs(graph,s=0):
	result=[s]
	que=[]
	que_w=[]
	for i in graph[s]:
		que.append(i[0])
		que_w.append(i)
	



	# l=len(x)
	# while len(x)>0:
	# 	a=min(x)
	# 	for i in graph[s]:
	# 		if i[1]==a:
	# 			g.append(i[0])
	# 			x.remove(a)
	# for t in range(l):
	# 	for i in graph[g[t+1]]:
	# 		x.append(i[1])
	# 	l1=len(x)
	# 	while len(x)>0:
	# 		a=min(x)
	# 		for i in graph[g[t+1]]:
	# 			if i[1]==a:
	# 				if i[0] not in g:
	# 					g.append(i[0])
	# 					x.remove(a)
						


	return que,que_w



if __name__=="__main__":
	points=int(input())
	w=lis(points)
	# print(lis(points))
	#print(Dijkstra(w,int(input("enter the source "))))
	print(bfs(w))