def insatind(l,pos,elem):
    if(pos in range(1,len(l),1)):
        m = len(l)-1
        l.append(0)
        for i in range(m,pos-2,-1):
            l[i+1] = l[i]
        l[pos-1] = elem
        print(l)
    else:
        print("Error!")

l = [1,3,4,5]
index = 2
element = 2

print("List after Insertion of",element,"at index",index,":")

insatind(l,index,element)

