strings = raw_input().split(" ")
N= int(strings[0])
H= int(strings[1])
strings1=raw_input().split(" ")
A= map(int, strings1)
maxi = A[0]
sumi = 0
for i in range(len(A)):
    sumi += A[i]
    if(maxi < A[i]):
        maxi = A[i]
flag=True
avg = sumi/H
low = avg
high = maxi
hr = 0
while(low<=high):
    mid = (low+high)/2
    hr = 0
    for j in range(len(A)):
        if( A[j]%mid != 0):
            hr += A[j]/mid + 1
        else:
            hr += A[j]/mid
    if(hr <= H):
        ans = mid
        high = mid - 1 
    else:
        low = mid  + 1  
print ans 