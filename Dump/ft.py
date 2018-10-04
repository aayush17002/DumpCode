import math
n,k = map(int,input().split())
array=list(map(int,input().split()))
if(array[0]>=k):
    size=1
else:
    size=0
msize=0
t=array[0]
for i in range(1,n):
    t=math.gcd(t,array[i]);
    if(t>=k):
        size+=1
    else:
        t=array[i]
        if(size>msize):
            msize=size
        if(array[i]>=k):
            size=1
        else:
            size=0
if(msize<size):
    msize=size
print(msize)