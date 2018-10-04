def flip(x):
	if(x==0):
		return 1
	else:
		return 0
m = [[1,1,1],[1,1,1],[1,1,1]]
A = list(map(int,input().split()))
if(A[0]%2==1):
	m[0][0] = flip(m[0][0])
	m[0][1] = flip(m[0][1])
	m[1][0] = flip(m[1][0])
if(A[1]%2==1):
	m[0][0] = flip(m[0][0])
	m[0][1] = flip(m[0][1])
	m[1][1] = flip(m[1][1])
	m[0][2] = flip(m[0][2])
if(A[2]%2==1):
	m[0][1] = flip(m[0][1])
	m[0][2] = flip(m[0][2])
	m[1][2] = flip(m[1][2])
A = list(map(int,input().split()))
if(A[0]%2==1):
	m[0][0] = flip(m[0][0])
	m[1][1] = flip(m[1][1])
	m[1][0] = flip(m[1][0])
	m[2][0] = flip(m[2][0])
if(A[1]%2==1):
	m[2][1] = flip(m[2][1])
	m[0][1] = flip(m[0][1])
	m[1][1] = flip(m[1][1])
	m[1][2] = flip(m[1][2])
	m[1][0] = flip(m[1][0])
if(A[2]%2==1):
	m[1][1] = flip(m[1][1])
	m[0][2] = flip(m[0][2])
	m[1][2] = flip(m[1][2])
	m[2][2] = flip(m[2][2])
A = list(map(int,input().split()))
if(A[0]%2==1):
	m[2][0] = flip(m[2][0])
	m[2][1] = flip(m[2][1])
	m[1][0] = flip(m[1][0])
if(A[1]%2==1):
	m[2][0] = flip(m[2][0])
	m[2][1] = flip(m[2][1])
	m[1][1] = flip(m[1][1])
	m[2][2] = flip(m[2][2])
if(A[2]%2==1):
	m[1][2] = flip(m[1][2])
	m[2][2] = flip(m[2][2])
	m[2][1] = flip(m[2][1])
for i in range(3):
	for j in m[i]:
		print(j,end="")
	print()