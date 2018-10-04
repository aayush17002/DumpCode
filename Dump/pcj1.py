def findLargestSumPair(arr, n):
    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]     
    else:
        first = arr[1]
        second = arr[0]
    if(n>2):
	    for i in range(2, n):
	        if arr[i] > first:
	            second = first
	            first = arr[i]
	        elif arr[i] > second and arr[i] != first:
	            second = arr[i]     
    return (first + second)
n = int(input())
A = list(map(int, input().split()))
if(n==1):
	print(A[0])
else:
	print(findLargestSumPair(A, n))