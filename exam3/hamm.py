def hamm(a,b):
	y=a^b
	h=0
	while(y>0):
		k=y%2
		if k==1:
			h+=1
		y=y//2
	print(h)
	return
hamm(4,1)
hamm(25,30)
hamm(100,250)
hamm(1,30)
hamm(0,255)