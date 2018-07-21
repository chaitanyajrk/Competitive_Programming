def cmb(d, d2):
    for i in d2:
        if i in d:
            d[i] += d2[i]
        else:
            d[i] = d2[i]
    return d

def molcl (yyyy):
    fml = {}
    sss = ""
    i=0
    while i < len(yyyy):
        if yyyy[i].isdigit() == True:
            if i + 1 < len(yyyy):
                if yyyy[i + 1].isdigit() == True:
                    fml[sss] += int(yyyy[i:i+2]) - 1
                    i+=1
                else:
                    fml[sss] += int(yyyy[i])-1
            else:
                fml[sss] += int(yyyy[i]) - 1
        elif yyyy[i] == ")" or yyyy[i] == "]" or yyyy[i] == "}":
            return [i+1, fml]
        elif yyyy[i] == "(" or yyyy[i] == "[" or yyyy[i] == "{":
            temp = molcl(yyyy[i+1:])
            i += temp[0]
            if i+1 < len(yyyy):
                if yyyy[i+1].isdigit()==True:
                    i+=1
                    for key, value in temp[1].items():
                        temp[1][key] = value * int(yyyy[i])
            fml = cmb(temp[1], fml)
        else:
            if yyyy[i].isupper()==True:
                if i+1 < len(yyyy):
                    if yyyy[i+1].islower()==True:
                        if yyyy[i:i+2] in fml:
                            fml[yyyy[i:i+2]]+=1
                            sss = yyyy[i:i+2]
                            i+=1
                        else:
                            fml[yyyy[i:i+2]] = 1
                            sss = yyyy[i:i+2]
                    else:
                        if yyyy[i] in fml:
                            fml[yyyy[i]] = 1
                            sss = yyyy[i]
                        else:
                            fml[yyyy[i]] = 1
                            sss = yyyy[i]
                else:
                    if yyyy[i] in fml:
                        fml[yyyy[i]] = 1
                        sss = yyyy[i]
                    else:
                        fml[yyyy[i]] = 1
                        sss = yyyy[i]
        i += 1
    return fml
print(molcl("NaOH"))
print(molcl("Mg(OH)2"))
print(molcl("H2O"))
print(molcl("K4(ON(SO3)2)2"))
print(molcl("C10H16O"))
print(molcl("Zn(NO3)2"))
print(molcl("F2"))