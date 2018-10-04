def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1 
    if (m == 1) :
        return 0 
    while (a > 1) :
        q = a // m 
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0) :
        x = x + m0 
    return x

n = int(input())
k = int(input())
m = 1000000007
q = 2**(n-1)
p = q-n
q = modInverse(q,m)
ans = (p*q)%m
print(ans)