"""Aayush Gupta 
2017002
5/10/2017"""

import copy
#for obtaining the graph
def lis(points):
	graph=[[] for i in range(points)]
	for i in range(points):
		connections=int(input())
		for t in range(connections):
			x=input().split()
			x=[int(x[0]),int(x[1])]
			graph[i].append(x)
	# for i in range(1,len(d)):
	# 	if len(d[i])>0:	
	# 		for j in range(len(d)):
	# 			if j!=i:
	# 				for t in range(len(d[i])):
	# 					if d[i][t][0]!=j:
	# 						for z in range(len(d[j])):
	# 							if d[j][z][0]==i:
	# 								x=[j,d[j][z][1]]
	# 								d[i].append(x)
	# 								break
	# 						break
	# 	else:
	# 		for j in range(len(d)):
	# 			if j!=i:
	# 				for t in range(len(d[j])):
	# 					if t!=i:
	# 						if d[j][t][0]==i:
	# 							x=[j,d[j][t][1]]
	# 							d[i].append(x)
	# 							break
	return graph

#for Dijkstra
def Dijkstra(graph,source=0):
	dist=[2000000 for i in range(len(graph))]
	dist[source]=0
	for v in graph[source]:
		for times in range(len(v)):
			if dist[v[0]]>v[1]:
				dist[v[0]]=v[1]
	y=copy.deepcopy(dist)
	for z in range(len(graph)*5):
		y[source]=2000000
		source=y.index(min(y))
		for v in graph[source]:
			for t in range(len(v)):
				if dist[v[0]]>v[1]+min(y):
					dist[v[0]]=v[1]+min(y)
	for v in range(len(dist)):
		if dist[v]==2000000:
			dist[v]="inf"
	return dist

# for Breath First Search
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
	return seq,weight
if __name__=="__main__":
	points=int(input())
	w=lis(points)
	print(Dijkstra(w,int(input("enter the source "))))
	print(Dijkstra(w,int(input("enter the source "))))
	print(Dijkstra(w,int(input("enter the source "))))
	print(Dijkstra(w,int(input("enter the source "))))
	print(Dijkstra(w,int(input("enter the source "))))
	print(bfs(w,int(input("enter the source "))))
	print(bfs(w,int(input("enter the source "))))
	print(bfs(w,int(input("enter the source "))))
	print(bfs(w,int(input("enter the source "))))
	print(bfs(w,int(input("enter the source "))))