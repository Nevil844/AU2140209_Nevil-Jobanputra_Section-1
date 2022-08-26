def insated(array,element):
    l=[0]*(len(array)+1)
    for i in range(len(array)):
        l[i]=x[i]
    l[len(array)]=element
    print(l)

x=[1,2,3,4]
insated(x,5)
