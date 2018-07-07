def ana(st1,st2):
	dic={}
	dic2={}
	st1=st1.lower()
	st2=st2.lower()
	st1=st1.replace(" ","")
	
	st2=st2.replace("\n","")
	st2=st2.replace(" ","")
	for i in  st1:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
	for i in st2:

		if i in dic2:
			dic2[i]+=1
		else:
			dic2[i]=1
	if dic==dic2:
		return True
	else:
		return  False

file=open("t1.txt","r")
for l in file:
	
	l=l.replace("\n","")


	r1=l.split(",")
	
	print(l+"------"+str(ana(r1[0],r1[1])))
	


