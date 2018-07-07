def path(list1):
	dic={}
	for i in range (7):
		dic[i]=[]
	vis=[0]*7
	tr=[]
	vis[0]=1
	
	kk=max(list1)
	# print(kk)
	
	m=max(kk)
	# print(m)
	tr.extend(list1[0])
	
	while len(tr)!=0:
		y=tr.pop()
		# print(y)
		if(y>=len(list1)):
			vis[y]=1
		
		if(y<len(list1)and vis[y]==0):
			vis[y]=1
			tr.extend(list1[y])
		# print(vis)
	for i in  range(m+1):
		if(vis[i]!=1):
			return  False	
	return True
print(path([[1], [0,2], [3]]))
print(path([[1,3], [3,0,1], [2], [0]]))
print(path([[1], [0,2], [3]]))
print(path([[1,3], [3,0,1], [2], [0]]))
print(path([[1,2,3], [0], [0], [0]]))
print(path([[1], [0,2,4], [1,3,4], [2], [1,2]]))
print(path([[1], [2,3], [1,2], [4], [1], [5]]))
print(path([[1], [2], [3], [4], [2]]))
print(path([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]))




