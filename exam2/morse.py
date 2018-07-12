

d={
	"A" :".-",
	"B":"-...",
	"C" :"-.-.",
	"D" :"-..",
	"E" :".",
	"F" :"..-.",
	"G" :"--.",
	"H" :"....",
	"I" :"..",
"J" :".---",
"K" :"-.-",
"L" :".-..",
"M" :"--",	
"N" :"-.",
"O" :"---",
"P" :".--.",
"Q" :"--.-",
"R" :".-.",
"S" :"...",
"T" :"-",
"U" :"..-",
"V" :"...-",
"W" :".--",
"X" :"-..-",
"Y" :"-.--",
"Z" :"--.."

}
def morse(li):
	global d
	y={}
	for i in li:
		temp=""
		for j in  i:
			temp=temp+d[j.upper()]
		if temp not in  y:
			y[temp]=1	


	print(len(y))
	return 0
words = ["gin", "zen", "gig", "msg"]
morse(words)
words = ["a", "z", "g", "m"]
morse(words)
words = ["bhi", "vsv", "sgh", "vbi"]
morse(words)
words = ["a", "b", "c", "d"]
morse(words)
words = ["hig", "sip", "pot"] 
morse(words)