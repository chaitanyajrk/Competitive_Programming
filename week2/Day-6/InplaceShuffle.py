import random

def shuffle(lis):

	# Shuffle the input in place
	if(len(lis)>1):
		for i in range(len(lis)):
			j = random.randint(i,len(lis)-1)
			if i!=j:
				lis[i],lis[j] = lis[j],lis[i]



sl = [1, 2, 3, 4, 5]
print 'list ', sl

print 'Shuffling list...'
shuffle(sl)
print sl
