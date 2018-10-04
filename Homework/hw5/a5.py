#to take the input of the array
def array_input():
	array_1=[]
	array_2=[]
	array1=input("enter the min terms: ").split()
	array2=input("enter the don't cares: ").split()
	a=int(input("enter the number of variables: "))
	n=2**a
	if len(array2)==n:
		print('x')
		exit()
	elif array1==[]:
		print(0)
		exit()
	
	for i in array1:
		array_1.append(int(i))
	array_1.sort()
	for i in array2:
		array_2.append(int(i))
	array_2.sort()
	for i in array1:
		if i in array2:
			return "not valid"
	return array_1,array_2,n
#to formulate the kind of kmap to be formed
def check_map_config(array1,array2):
	l1=len(array1)
	l2=len(array2)
	if l1>0 and l2>0:
		last=max(array1[l1-1],array2[l2-1])
	elif l2==0 and l1==0:
		last=0
	elif l1>0 and l2==0:
		last=array1[l1-1]
	elif l2>0 and l1==0:
		last=array2[l2-1]
	if last<2:
		return 2
	elif last<4:
		return 4
	elif last<8:
		return 8
	elif last<16:
		return 16
	elif last<32:
		return 32
#to form the kmap
def matrix_former(array1,array2,n):
	if n==2:
		l=[[0,0]]
		for i in array1:
			l[0][int(i)]=1
		for i in array2:
			l[0][int(i)]='x'
	elif n==4:
		l=[[0,0],[0,0]]
		for i in array1:
			if int(i)<2:
				l[0][int(i)]=1
			else:
				l[1][int(i)-2]=1
		for i in array2:
			if int(i)<2:
				l[0][int(i)]='x'
			else:
				l[1][int(i)-2]='x'
	elif n==8:
		l=[[0,0,0,0],[0,0,0,0]]
		for i in array1:
			if int(i)<2:
				l[0][int(i)]=1
			elif int(i)==2:
				l[0][3]=1
			elif int(i)==3:
				l[0][2]=1
			elif int(i)<6:
				l[1][int(i)-4]=1
			elif int(i)==6:
				l[1][3]=1
			elif int(i)==7:
				l[1][2]=1
		for i in array2:
			if int(i)<2:
				l[0][int(i)]='x'
			elif int(i)==2:
				l[0][3]='x'
			elif int(i)==3:
				l[0][2]='x'
			elif int(i)<6:
				l[1][int(i)-4]='x'
			elif int(i)==6:
				l[1][3]='x'
			elif int(i)==7:
				l[1][2]='x'
	elif n==16:
		l=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		for i in array1:
			if int(i)<2:
				l[0][int(i)]=1
			elif int(i)==2:
				l[0][3]=1
			elif int(i)==3:
				l[0][2]=1
			elif int(i)<6:
				l[1][int(i)-4]=1
			elif int(i)==6:
				l[1][3]=1
			elif int(i)==7:
				l[1][2]=1
			elif int(i)<10:
				l[3][int(i)-8]=1
			elif int(i)==10:
				l[3][3]=1
			elif int(i)==11:
				l[3][2]=1
			elif int(i)<14:
				l[2][int(i)-12]=1
			elif int(i)==14:
				l[2][3]=1
			elif int(i)==15:
				l[2][2]=1
		for i in array2:
			if int(i)<2:
				l[0][int(i)]='x'
			elif int(i)==2:
				l[0][3]='x'
			elif int(i)==3:
				l[0][2]='x'
			elif int(i)<6:
				l[1][int(i)-4]='x'
			elif int(i)==6:
				l[1][3]='x'
			elif int(i)==7:
				l[1][2]='x'
			elif int(i)<10:
				l[3][int(i)-8]='x'
			elif int(i)==10:
				l[3][3]='x'
			elif int(i)==11:
				l[3][2]='x'
			elif int(i)<14:
				l[2][int(i)-12]='x'
			elif int(i)==14:
				l[2][3]='x'
			elif int(i)==15:
				l[2][2]='x'
	elif n==32:
		l=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
		for i in array1:
			if int(i)<2:
				l[0][int(i)]=1
			elif int(i)==2:
				l[0][3]=1
			elif int(i)==3:
				l[0][2]=1
			elif int(i)==4:
				l[0][7]=1
			elif int(i)==5:
				l[0][6]=1
			elif int(i)==6:
				l[0][4]=1
			elif int(i)==7:
				l[0][5]=1
			elif int(i)<10:
				l[1][int(i)-8]=1
			elif int(i)==10:
				l[1][3]=1
			elif int(i)==11:
				l[1][2]=1
			elif int(i)==12:
				l[1][7]=1
			elif int(i)==13:
				l[1][6]=1
			elif int(i)==14:
				l[1][4]=1
			elif int(i)==15:
				l[1][5]=1
			elif int(i)<18:
				l[3][int(i)-16]=1
			elif int(i)==18:
				l[3][3]=1
			elif int(i)==19:
				l[3][2]=1
			elif int(i)==20:
				l[3][7]=1
			elif int(i)==21:
				l[3][6]=1
			elif int(i)==22:
				l[3][4]=1
			elif int(i)==23:
				l[3][5]=1
			elif int(i)<26:
				l[2][int(i)-24]=1
			elif int(i)==26:
				l[2][3]=1
			elif int(i)==27:
				l[2][2]=1
			elif int(i)==28:
				l[2][7]=1
			elif int(i)==29:
				l[2][6]=1
			elif int(i)==30:
				l[2][4]=1
			elif int(i)==31:
				l[2][5]=1
		for i in array2:
			if int(i)<2:
				l[0][int(i)]='x'
			elif int(i)==2:
				l[0][3]='x'
			elif int(i)==3:
				l[0][2]='x'
			elif int(i)==4:
				l[0][7]='x'
			elif int(i)==5:
				l[0][6]='x'
			elif int(i)==6:
				l[0][4]='x'
			elif int(i)==7:
				l[0][5]='x'
			elif int(i)<10:
				l[1][int(i)-8]='x'
			elif int(i)==10:
				l[1][3]='x'
			elif int(i)==11:
				l[1][2]='x'
			elif int(i)==12:
				l[1][7]='x'
			elif int(i)==13:
				l[1][6]='x'
			elif int(i)==14:
				l[1][4]='x'
			elif int(i)==15:
				l[1][5]='x'
			elif int(i)<18:
				l[3][int(i)-16]='x'
			elif int(i)==18:
				l[3][3]='x'
			elif int(i)==19:
				l[3][2]='x'
			elif int(i)==20:
				l[3][7]='x'
			elif int(i)==21:
				l[3][6]='x'
			elif int(i)==22:
				l[3][4]='x'
			elif int(i)==23:
				l[3][5]='x'
			elif int(i)<26:
				l[2][int(i)-24]='x'
			elif int(i)==26:
				l[2][3]='x'
			elif int(i)==27:
				l[2][2]='x'
			elif int(i)==28:
				l[2][7]='x'
			elif int(i)==29:
				l[2][6]='x'
			elif int(i)==30:
				l[2][4]='x'
			elif int(i)==31:
				l[2][5]='x'
	return l
#to evaluate the kmap
def downcheck(matrix,i,j):
	l=len(matrix)-1
	if i!=l:
		if matrix[i+1][j]==1 or matrix[i+1][j]=='x':
			return True
		else:
			return False
	else:
		if matrix[0][j]==1 or matrix[0][j]=='x':
			return True
		else:
			return False
def rightcheck(matrix,i,j):
	l=len(matrix[i])-1
	if j!=l:
		if matrix[i][j+1]==1 or matrix[i][j+1]=='x':
			return True
		else:
			return False
	else:
		if matrix[i][0]==1 or matrix[i][0]=='x':
			return True
		else:
			return False
#detail about occurances
def col_row(matrix):
	count_c={}
	for j in range(len(matrix[0])):
		for i in range(len(matrix)):
			if (matrix[i][j]==1 or matrix[i][j]=='x') and downcheck(matrix,i,j):
				if i!=len(matrix)-1:
					if int(j) not in count_c.keys():
						count_c[int(j)]=[i,i+1]
					else:
						if i not in count_c[int(j)]:
							a=[i,i+1]
							count_c[int(j)].extend(a)
						else:
							count_c[int(j)].append(int(i+1))
					# print(count_c)
				else:
					if int(j) not in count_c.keys():
						count_c[int(j)]=[i,0]
					else:
						if i not in count_c[int(j)]:
							if 0 not in count_c[int(j)]:
								a=[i,0]
								count_c[int(j)].extend(a)
							else:
								count_c[int(j)].append(int(i))
							# print(count_c)
						else:
							if 0 not in count_c[int(j)]:
								count_c[int(j)].append(0)
				# print(count_c)
	count_r={}
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if (matrix[i][j]==1 or matrix[i][j]=='x') and rightcheck(matrix,i,j):
				if j!=len(matrix[0])-1:
					if int(i) not in count_r.keys():
						count_r[int(i)]=[j,j+1]
					else:
						if int(j) not in count_r[int(i)]:
							a=[j,j+1]
							count_r[int(i)].extend(a)
						else:
							count_r[int(i)].append(int(j+1))
					# print(count_r)
				else:
					if int(i) not in count_r.keys():
						count_r[int(i)]=[j,0]
					else:
						if int(j) not in count_r[i]:
							if 0 not in count_r[i]:
								a=[j,0]
								count_r[int(i)].extend(a)
							else:
								count_r[int(i)].append(int(j))
						else:
							if 0 not in count_r[i]:
								count_r[int(j)].append(0)

				# print(count_r)
	return (count_c,count_r)
#solver
def kmap(matrix,col,row,n):
	if n==2:
		if row!={}:
			return 1
		else:
			col_l=list(col.keys())
			if 0 in col_l:
				return '~A'
			else:
				return 'A'
	elif n==4:
		ans=""
		if col!={} and row!={}:
			col_l=list(col.keys())
			row_l=list(row.keys())
			if len(col_l)==2:
				return 1
			else:
				if 0 in row_l:
					if ans!="":
						ans+='+ ~A '
					else:
						ans+='~A '
				else:
					if ans!="":
						ans+='+ A '
					else:
						ans+='A '
				if 0 in col_l:
					if ans!="":
						ans+='+ ~B '
					else:
						ans+='~B '
				else:
					if ans!="":
						ans+='+ B '
					else:
						ans+='B '
		elif col=={} and row!={}:
			row_l=list(row.keys())
			if 0 in row_l:
				if ans!="":
					ans+='+ ~A '
				else:
					ans+='~A '
			else:
				if ans!="":
					ans+='+ A '
				else:
					ans+='A '
		elif col!={} and row=={}:
			col_l=list(col.keys())
			if 0 in col_l:
				if ans!="":
					ans+='+ ~B '
				else:
					ans+='~B '
			else:
				if ans!="":
					ans+='+ B '
				else:
					ans+='B '
		else:
			if matrix[0][0]==1:
				ans+='~A~B '
			if matrix[0][1]==1:
				ans+='~AB '
			if matrix[1][0]==1:
				if ans=='':
					ans+='A~B'
				else:
					ans+='+ A~B'
			if matrix[1][1]==1:
				if ans=='':
					ans+='AB'
				else:
					ans+='+ AB'
		return ans


array1,array2,n=array_input()
# print(array1,array2)
n1=check_map_config(array1,array2)
assert n>=n1, "enter a valid matrix or correspondig min terms"
print(n)
A=matrix_former(array1,array2,n)
print(A)
col,row=col_row(A)
print(col)
print(row)
print(kmap(A,col,row,n))