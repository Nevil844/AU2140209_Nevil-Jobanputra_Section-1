def srch(l,a):
    for i in range(len(l)):
        if(l[i]==a):
            return i+1
    return -1
print(srch([1,4,3,2,],3))