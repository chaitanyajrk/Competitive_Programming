def elv(l):
	i=2
	un=0
	while(i<len(l)-1):
		a=l[i-1]
		b=l[i+1]
		# print(a,b)
		# print(i)
		if  i==2:
			if a>b:
				m=max(l[i+1:])
				for k  in range(i+1,len(l)):
					if  l[k]==m:
						pos=k
					# print("posn")
					# print(pos)
				for  k in  range(i,pos):
					# print(un)
					# if(i>7):
						# print("kostundi")
						# print(k)				
					un+=min(a,m)-l[k]
				i=pos+2
				if i>=len(l)-1:
					i=len(l)-2


			else:	
				k=min(a,b)
				if(l[i]<k):
					un+=k-l[i]
				i+=2
		else:
			if(a<b):
				x=l[i-2]
				if(x>a):
					i=i-1
					continue



			m=max(l[i+1:])
			# print(m)
			# print("solo")
			for k  in range(i+1,len(l)):
				if  l[k]==m:
					pos=k
					# print("posn")
					# print(pos)
			for  k in  range(i,pos):
				# print(un)
				un+=min(a,m)-l[k]
				# if(pos!=6):
				# 	print("kostundi")
				# 	print(k,un)


				
			i=pos+2
			# print(pos)
			# print(i)
	print(un)	





	return
k=[0, 1, 0, 2, 1, 0, 1]

elv(k)	
y=	[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
elv(y)
z=[0, 1, 0, 2, 1, 0, 5, 1, 0, 2]
elv(z)

ss=[0, 1, 0, 5, 1, 0, 2]
elv(ss)
tt=[0, 5, 1, 3, 4, 0, 1]
elv(tt)