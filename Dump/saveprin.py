T = int(input())
for _ in range(T):
    n = int(input())
    val = list(map(int,input().split()))
    p = list(map(int,input().split()))
    ans = 0
    total = sum(val)
    dp = [0 for i in range(total+1)]
    temp = [0 for i in range(total+1)]
    dp[0] = 1-(p[0]/100)
    dp[val[0]] = p[0]/100
    for i in range(1,n):
        dp,temp = temp,dp
        dp = [0 for j in range(total+1)]
        for x in range(total):
            if(temp[x]==0):
                continue
            if(x+val[i]>total):
                continue
            dp[x] = dp[x]+temp[x]*(1-(p[i]/100))
            dp[x+val[i]] = temp[x]*(p[i]/100)
    ans = 0
    start = total//2 + total%2
    for i in range(start,total+1):
        ans += dp[i]
    print('{0:.7f}'.format(ans))