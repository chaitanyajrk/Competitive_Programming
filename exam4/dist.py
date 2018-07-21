def dis(n):
	y=bin(n)
	d=1
	mi=0
	fl=0
	if(n>0):
		y=y[2:]
	else:
		y=y[3:]
	for i in y:
		if(int(i)==1):
			fl+=1
			if(d>mi):
				mi=d
			d=1
		else:
			d+=1
	if(fl>=2):
		return mi
	else :
		return 0

print(dis(55))
print(dis(-5))
print(dis(12354))
print(dis(6))
print(dis(22))
print(dis(0))
print(dis(256))


