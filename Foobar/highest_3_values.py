#highest 3 values in dictioary
def f(d):
	h=dict(d)
	val=list(d.values())
	val.sort(reverse=True)
	return val[0],val[1],val[2]
if __name__ == '__main__':
	d={1:2,2:100,3:30,4:50}
	print(f(d))