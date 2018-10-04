n,k = map(int,input().split())
C = list(map(int,input().split()))
C.sort(reverse=True)
cnt = 0
ans = 0
for i in range(n):
	ans += C[i]*(cnt//k+1)
	cnt += 1
print(ans)