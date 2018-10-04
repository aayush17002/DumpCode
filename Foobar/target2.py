import math
combinations=[]
count_p1=0
count_p2=0
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    global combinations
    if s == target: 
    	if partial not in combinations:
    		combinations.append(partial)
    	# print(partial)
    elif s >= target:
        return  # if we reach the number why bother to continue
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


def c(a,b,c=1):
	a=math.factorial(a)
	b=math.factorial(b)
	c=math.factorial(c)
	return (a//b)//c

def count(combinations):
	global count_p1,count_p2
	list_c=combinations[0]
	c1=0
	c2=0
	c4=0
	num=0
	for i in list_c:
		if i==1:
			c1+=1
		elif i==2:
			c2+=1
		elif i==4:
			c4+=1
		num+=1
	# print(c1,c2,c4)
	# print(num)
	if c1!=0:
		if c2!=0:
			if c4!=0:#c1,c2,c4
				axe=(math.factorial(num))//(math.factorial(c1)*math.factorial(c2)*math.factorial(c4))
				# print(axe)
				if num%2==0:
					count_p2+=axe
				else:
					count_p1+=axe
					print(c1,c2,c4)
					print(num)
					print(axe)
			else:#c1,c2
				axe=(math.factorial(num))//(math.factorial(c1)*math.factorial(c2))
				# print(axe)
				if num%2==0:
					count_p2+=axe
				else:
					count_p1+=axe
					print(c1,c2,c4)
					print(num)
					print(axe)
		else:
			if c4!=0:#c1,c4
				axe=(math.factorial(num))//(math.factorial(c1)*math.factorial(c4))
				# print(axe)
				if num%2==0:
					count_p2+=axe
				else:
					count_p1+=axe
					print(c1,c2,c4)
					print(num)
					print(axe)

			else:#c1
				if num%2==0:
					count_p2+=1
				else:
					count_p1+=1
	elif c2!=0:
		if c4!=0:#c2,c4
			axe=(math.factorial(num))//(math.factorial(c2)*math.factorial(c4))
			# print(axe)
			if num%2==0:
				count_p2+=axe
			else:
				count_p1+=axe
				print(c1,c2,c4)
				print(num)
				print(axe)
		else:#c2
			if num%2==0:
				count_p2+=1
			else:
				count_p1+=1
	elif c4!=0:#c4
		if num%2==0:
			count_p2+=1
		else:
			count_p1+=1
	del combinations[0]
	if len(combinations)>0:
		count(combinations)


if __name__ == "__main__":
	t=input().split()
	coins=int(t[0])
	lis=[]
	for i in range(coins):
		lis.append(1)
	for i in range(coins//2):
		lis.append(2)
	for i in range(coins//4):
		lis.append(4)
	print(lis,coins)
	subset_sum(lis, coins)
    # print(combinations)
	count(combinations)
	print(int(count_p1),int(count_p2))