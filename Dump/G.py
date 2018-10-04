V = int(input())
graph = [0 for _ in range(V)]
for i in range(V):
	graph[i] = list(input())
for i in range(V):
	for j in range(V):
		graph[i][j] = int(graph[i][j])
for i in range(V-1):
	for j in range(i+1,V):
		if(graph[i][j]!=graph[j][i]):
			graph[i][j] = 1
			graph[j][i] = 1
n = 3
def DFS(graph, marked, n, vert, start, count):
	marked[vert] = True
	if n == 0: 
		marked[vert] = False
		if graph[vert][start] == 1:
			count = count + 1
			return count
		else:
			return count
	for i in range(V):
		if marked[i] == False and graph[vert][i] == 1:
			count = DFS(graph, marked, n-1, i, start, count)
	marked[vert] = False
	return count
def countCycles( graph, n):
	marked = [False] * V
	count = 0
	for i in range(V-(n-1)):
		count = DFS(graph, marked, n-1, i, i, count)
		marked[i] = True
	return int(count/2)
print(countCycles(graph, n))