def insatbeg(array,element):
    l=[0]*(len(array)+1)
    for i in range(len(array)):
        l[i+1]=x[i]
    l[0]=element
    print(l)

x=[2,3,4]
insatbeg(x,1)

