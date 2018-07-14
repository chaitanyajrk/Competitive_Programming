def eggs(number):
	chk=14
	x=0
	y=0
	while x<number:
		y=x
		x=x+chk
		chk=chk-1
		print(x,end=",")
		
	for k1 in range(y+1,number+1):
		print(k1,end=",")


eggs(15)	