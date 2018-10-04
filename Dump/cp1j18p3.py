def function(n):
	if (n == 0):
		return 0
	else:
		val = function(n&(n-1))
		return 1+val

def function2(l,r,A):
	result = 0
	for i in range(l,r+1):
		result = result + function(A[i])
	return result

N,Q = map(int,input().split())
A = [0 for y in range(N+1)]
# print(A)
for i in range(Q):
	B = list(map(int,input().split()))
	if(B[0]==1):
		A[B[1]] = 2*A[B[1]] + 1
	elif(B[0]==2):
		A[B[1]] = A[B[1]]//2
	else:
		val = function2(B[1],B[2],A)
		print(val)
# print(A)