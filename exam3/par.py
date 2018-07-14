global res_ls
def com(ls, pos, n, obr, cl):
    # print (ls,pos,n,obr,cl)
    if cl==n:
        s=''
        for i in range(len(ls)):
            s+=ls[i]
            # print(s)
        res_ls.append(s)
        # print("--")
        return
    else:
        if obr > cl :
            ls[pos]='}'
             # print(s)
            com(ls,pos+1,n,obr,cl+1)
        if obr <n:
             # print(s)
            ls[pos]='{'
             # print(s)
              # print(s)
               # print(s)
            com(ls,pos+1,n,obr+1,cl)


def prs(n):
    global res_ls
    res_ls=[]
    parenthesis_ls=[None]*(2*n)
    com(parenthesis_ls,0,n,0,0)
    print (res_ls,len(res_ls))
    pass
def frs(l):
    for i  in  l:
        prs(i)
    pass

frs([2,3,5,4,1,6])