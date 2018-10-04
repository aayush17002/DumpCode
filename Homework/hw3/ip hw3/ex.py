def distance(con,weights):
	con=eval(con)
	weights=eval(weights)
	dic=[]
	if len(con)==len(weights):
		for i in range(len(con)):
			dic.append(dict(zip(con[i], weights[i])))
			# if con[i]==[]:
			# 	dic.pop(i)
			# 	d={i+1:100000}
			# 	dic.append(d)
	#print(dic)
	for i in range(1,len(dic)):
		for t in range(len(dic)):
			if dic[i].get(t)==None:
				if dic[t].get(i)!=None:
					x={t:(dic[t].get(i))}
					dic[i].update(x)
	for i in range(len(dic)):
		x={i:0}
		dic[i].update(x)
	return dic
	

def ans(dic,s,e):
	a=[ 0 for i in range(6)]
	if s==e:
		return 0
	elif s>e:
		for i in dic[s]:
			if i==e:
				return dic[s].get(i1)
		for i in dic[s]:
			if s-5>i>e:
				a[0]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[0]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i>i1>e:
						a[0]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[0]+=dic[i1].get(i2)
			elif s-4>i>e:
				a[1]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[1]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i>i1>e:
						a[1]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[1]+=dic[i1].get(i2)
			elif s-3>i>e:
				a[2]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[2]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i>i1>e:
						a[2]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[2]+=dic[i1].get(i2)
			elif s-2>i>e:
				a[3]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[3]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i>i1>e:
						a[3]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[3]+=dic[i1].get(i2)
			elif s-1>i>e:
				a[4]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[4]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i>i1>e:
						a[4]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[4]+=dic[i1].get(i2)
			elif s>i>e:
				a[5]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[5]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i>i1>e:
						a[5]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[5]+=dic[i1].get(i2)
		x=[]
		for i in a:
			if i!=0:
				x.append(i)
		return min(x)

	elif s<e:
		for i in dic[s]:
			if i==e:
				return dic[s].get(i)
		for i in dic[s]:
			if s+5<i<e:
				a[0]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[0]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i<i1<e:
						a[0]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[0]+=dic[i1].get(i2)
			elif s+4<i<e:
				a[1]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[1]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i<i1<e:
						a[1]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[1]+=dic[i1].get(i2)
			elif s+3<i<e:
				a[2]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[2]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i<i1<e:
						a[2]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[2]+=dic[i1].get(i2)
			elif s+2<i<e:
				a[3]=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[3]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i<i1<e:
						a[3]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[3]+=dic[i1].get(i2)
			elif s+1<i<e:
				a[4]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[4]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i<i1<e:
						a[4]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[4]+=dic[i1].get(i2)
								
			elif s<i<e:
				a[5]+=dic[s].get(i)
				for i1 in dic[i]:
					if i1==e:
						a[5]+=dic[i].get(i1)
						break
				for i1 in dic[s]:
					if i<i1<e:
						a[5]+=dic[i].get(i1)
						for i2 in dic[i1]:
							if i2==e:
								a[5]+=dic[i1].get(i2)
		
		x=[]
		for i in a:
			if i!=0:
				x.append(i)
		return min(x)

if __name__=="__main__":
	c=input('connections: ')
	w=input("weights: ")
	again=True
	while again:
		print(ans(distance(c,w),int(input("start: ")),int(input("end: "))))
		z=input("do you want it again: y/n ")
		if z[0]=='y':
			again=True
		else:
			again=False