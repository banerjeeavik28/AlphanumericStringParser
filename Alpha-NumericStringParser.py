def AlphnumStrPar(S, K):
    d = 0
    if("--" in  S):
        S = S.replace("--", "-")
        print(S)
    j = S.split("-")
    #print(j)
    z = ""
    for i in range(len(j)):
        z = z + j[i]
    print(z)
    for y in range(len(z)):
        if((ord(z[y+d]) >= 97) or (ord(z[y+d]) <= 122)):
            z = z.replace(z[y+d],z[y+d].upper())
        if(K == 0):
            continue
        elif(K<0):
            continue
        elif(K != int(K)):
            continue
        elif(((y+1)%K) == 0):
            #list(z)
            z = z[:y+d]+ z[y+d].replace(z[y+d],z[y+d]+"-") + z[y+d+1:]
            #z = z.replace(z[y], z[y] + "-")
            d = d+1
        if(z[len(z)-1] == "-"):
            z = z[:len(z)-1]+ z[len(z)-1].replace(z[len(z)-1],"")  
    print(type(z))
    return z