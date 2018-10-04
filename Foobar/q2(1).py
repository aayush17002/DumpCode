from random import uniform 
from copy import deepcopy
def selection_sort(array):
	swap=0
	compare=0
	l=len(array)
	for i in range(l):
		min_t=array[i]
		t=[]
		if i+1<l:
			for j in range(i+1,l):
				compare+=1
				t.append(array[j])
			x=min(t)
		if x<min_t:
			min_t=x
			index_m=array.index(x)
			swap+=1
			array[i],array[index_m]=array[index_m],array[i]
	# print(array)
	# print(compare)
	# print(swap)
	return compare

def insertion_sort(array):
	compare=0
	swap=0
	for i in array:
		j = array.index(i)
		while j>0:
			compare+=1
			if array[j-1]>array[j]:
				swap+=1
				array[j-1],array[j] = array[j],array[j-1]				
			else:
				break
			j = j-1
	# print (array)
	# print(compare)
	# print(swap)
	return compare

def Merge_Sort(nlist):
	global compare
	if len(nlist)>1:
		mid = len(nlist)//2
		lefthalf = nlist[:mid]
		righthalf = nlist[mid:]
		Merge_Sort(lefthalf)
		Merge_Sort(righthalf)
		i=j=k=0       
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				nlist[k]=lefthalf[i]
				i=i+1
				compare+=1
			else:
				nlist[k]=righthalf[j]
				j=j+1
				compare+=1
			k=k+1
		while i < len(lefthalf):
			nlist[k]=lefthalf[i]
			i=i+1
			k=k+1
		while j < len(righthalf):
			nlist[k]=righthalf[j]
			j=j+1
			k=k+1 

if __name__=="__main__":
	a=0
	b=0
	c=0
	ap=0
	for k in range(100):
		t=[10]
		w=len(t)
		for j in t:		
			array1=[]
			for i in range(j):
				x=uniform(-100,100)
				array1.append(x)
			array=deepcopy(array1)
			a+=selection_sort(array)
			array=deepcopy(array1)
			b+=insertion_sort(array)
			array=deepcopy(array1)
			compare=0
			Merge_Sort(array)
			c+=compare
		ap+=1
	print("selection sort",a/(w*ap),"\n"+"insertion sort",b/(w*ap),"\n"+"merge sort",c/(w*ap))