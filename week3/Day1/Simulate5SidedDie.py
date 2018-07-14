import random


def rand7():
	return random.randint(1, 7)


def rand5():

	d=1
	while (d==1):
		i = rand7()
		if i<=5:
			return i	


print('Rolling 5-sided die...')
print(rand5())