t=int(input())
array=list(map(int,input().split()))
even=[]
odd=[]
x1=[]
x2=[]
for i in range(len(array)):
	if array[i]%2==0:
		even.append(i)
		x1.append(array[i])
	else:
		odd.append(i)
		x2.append(array[i])
x1.extend(x2)
count=0
# if 0 in even:
# 	l=even[1]
# 	r=even[len(even)-1]
# 	print(l,r)
# 	if len(even)>2 and len(odd)>2:
# 		for i in odd:
# 			if l<i<r:
# 				count+=1
# 	else:
# 		count=1
# else:
# 	l=even[0]
# 	r=even[len(even)-1]
# 	if len(even)>2 and len(odd)>2:
# 		for i in odd:
# 			if l<i<r:
# 				count+=1
# 	else:
# 		count=1

# print(count)
print(x1)