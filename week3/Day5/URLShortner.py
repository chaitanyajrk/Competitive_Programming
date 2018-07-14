def bcon(str1):
	dic={}
	for i in range(len(str1)):
		dic[i]=str1[i]
	return dic


shrtlen = 7
shrtdic={}
lngdic={}
count=0
base_62=bcon("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def URL_Shortnermethod(Given_URL):
	if (Given_URL in lngdic):
		print("ShortURL Exists"+lngdic[Given_URL])
		return
	global count
	s=""
	k=count
	count+=1

	if (k==0):
		s="0000000"
		if (s not in shrtdic):
			shrtdic[s]=Given_URL
			lngdic[Given_URL]=s
			print("short URL for "+Given_URL+" is https://ca.ke/"+s)
			return

	while(k!=0):
		s=base_62[k%62]+s
		k=k//62
	l=len(s)

	if (l<shrtlen):
		for i in range(shrtlen-l):
			s="0"+s

	if (s not in shrtdic):
		shrtdic[s]=Given_URL
		lngdic[Given_URL]=s

	print("Shortened URL for "+Given_URL+" is https://ca.ke/"+s)

while (True):
	print("Whatdo u  want to  do")
	print("\n\t1)Generate ShortURL\n\t2)Redirect ShortURL\n\t3)Stop\n\tYour option:",end="")
	i=int(input())
	if (i==1):
		Given_URL=input("Enter URL: ")
		URL_Shortnermethod(Given_URL)
	elif (i==2):
		Correct_URL=input("Enter a short URL: ")
		if shrtdic.get(Correct_URL,None) is not None:
			print("Redirect to "+shrtdic[Correct_URL])
		else:
			print("URL does not exist")
	elif(i==3):
		print("thanks for using us")
		break
	else:
		print("valid inputneed")