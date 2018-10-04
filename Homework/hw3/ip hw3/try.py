def distance(con,weights,start,end):
	con=eval(con)
	weights=eval(weights)
	dic=[]
	if len(con)==len(weights):
		for i in range(len(con)):
			dic.append(dict(zip(con[i], weights[i])))
			if con[i]==[]:
				dic.pop(i)
				d={i+1:100000}
				dic.append(d)
	for i in range(len(dic)):
		for t in range(len(dic)):
			if dic[i].get(t)==None:
				x={t:100000}
				dic[i].update(x)
	if start==0:
		if end==0:
			print(start,"to",end,"= 0")
		elif end==1:
			d1=min(dic[0].get(1),dic[0].get(2)+dic[2].get(1))
			print(start,"to",end,"=",d1)
		elif end==2:
			d2=min(dic[0].get(2),dic[0].get(1)+dic[1].get(2))
			print(start,"to",end,"=",d2)
		elif end==3:
			d3=min(dic[0].get(1)+dic[1].get(3),dic[0].get(2)+dic[2].get(3),dic[0].get(1)+dic[1].get(2)+dic[2].get(3),dic[0].get(2)+dic[2].get(1)+dic[1].get(3))
			print(start,"to",end,"=",d3)
		elif end==4:
			d4=min(dic[0].get(1)+dic[1].get(4),dic[0].get(1)+dic[1].get(3)+dic[3].get(4),dic[0].get(2)+dic[2].get(4),dic[0].get(2)+dic[2].get(3)+dic[3].get(4))
			print(start,"to",end,"=",d4)	
	# # d1=min(dic[0].get(1),dic[0].get(2)+dic[2].get(1))
	# # d2=min(dic[0].get(2),dic[0].get(1)+dic[1].get(2))
	# # d3=min(dic[0].get(1)+dic[1].get(3),dic[0].get(2)+dic[2].get(3))
	# # d4=min(dic[0].get(1)+dic[1].get(4),dic[0].get(1)+dic[1].get(3)+dic[3].get(4),dic[0].get(2)+dic[2].get(4),dic[0].get(2)+dic[2].get(3)+dic[3].get(4))
	# # print("1 = ",d1)
	# print("2 = ",d2)
	# print("3 = ",d3)
	# print("4 = ",d4)
if __name__=="__main__":
	c=input('connections: ')
	w=input("weights: ")
	s=int(input("start: "))
	e=int(input("end: "))
	distance(c,w,0,e)