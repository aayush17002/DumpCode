def sumx(n):
	if n==1:
		return 1
	else:
		return sumx(n-1)+n
print(sumx(int(input())))