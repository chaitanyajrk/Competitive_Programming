def qu(l):
	fl=[0]*len(l)
	l=sorted(l)
	l.reverse()

	co=0
	d=[]
	for i in  l:
		if  fl[i[1]]==0:
			fl[i[1]]=i
		else:
			a=fl[i[1]]
			b=i
			if a[0]<b[0]:
				fl[i[1]]=a
			else:
				fl[i[1]]=b
	# print(fl)
	k=[]
	for i in l:
		if i not in fl:
			d.append(i)
		if i!=0  and i not in d:
			k.append(i)
	# print(d)
	d.reverse()
	fl=k
	fl=sorted(fl)
	fl.reverse()
	# print(fl)
	for i in fl:
		if i!=0:
			d.insert(i[1],i)
	print(d)
	
	

	


l1=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
l2=[[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]
l3=[ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]
qu(l2)
qu(l3)
qu(l1)