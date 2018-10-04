import math
def summer(a,b):
	val = 0
	for i in range(len(a)):
		val = val+a[i]*b[i]
	return val
t = int(input())
for i in range(t):
	inn = list(map(float,input().split()))
	p = [0]*3
	q = [0]*3
	d = [0]*3
	c = [0]*3	
	for j in range(0,3):
		p[j] = inn[j]
	for j in range(3,6):
		q[j-3] = inn[j]-p[j-3]
	for j in range(6,9):
		d[j-6] = inn[j]
	for j in range(9,12):
		c[j-9] = inn[j]-p[j-9]
	r = inn[12]
	di_square = summer(d,d)
	di_ci = summer(d,c)
	ci_square = summer(c,c)-(r**2)
	qi_ci = summer(q,c)
	di_qi = summer(d,q)
	qi_square = summer(q,q)
	A = di_square - ((di_ci**2)/(ci_square))
	B = 2*(di_qi-(qi_ci/ci_square)*(di_ci))
	C = qi_square-((qi_ci**2)/ci_square)
	time = 0
	if(A!=0):
		part1 = -(B/(2*A))
		part2 = (math.sqrt((B**2)-(4*A*C)))/(2*A)
		t1 = part1+part2
		t2 = part1-part2
		if(t1>=0 and t2>=0):
			time = min(t1,t2)
		elif(t2>=0):
			time = t2
		else:
			time = t1
	else:
		time = -(C/B)
	print("%.10f" % time)