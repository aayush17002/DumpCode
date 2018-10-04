t=int(input())
array=list(map(int,input().split()))
count=0
for i in range(len(array)):
	if array[i]%2==1:
		for j in range(len(array)-1,i,-1):
			if array[j]%2==0:
				temp=array[i]
				array[i]=array[j]
				array[j]=temp
				count+=1
				break
print(count)