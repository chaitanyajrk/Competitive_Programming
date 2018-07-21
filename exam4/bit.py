def cnt(num):
#print(l)
    l=[]
    for i in range(num+1):
        n=bin(i)
        count=0
        for j in range(len(n)):
            if(n[j]=='1'):
            	count=count+1
        l.append(count)
    return  l

print(cnt(1))
print(cnt(25))
print(cnt(5))
print(cnt(6))
print(cnt(15))
print(cnt(16))


