list1=[1,2,3,4,6,7,5,10]
list2=[2,4,6,8,10]
list3=[]
def common_numbers(list1,list2):
	for x in list1:
		for y in list2:
			if x==y:
				list3.append(x)
	return list3
new=common_numbers(list1,list2)
print(new)
