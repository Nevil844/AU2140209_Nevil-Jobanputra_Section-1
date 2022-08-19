def prodArray(l):
    if(len(l)==0):
        return 1
    else:
        return l[0]*prodArray(l[1:])

print(prodArray([2,5,10]))