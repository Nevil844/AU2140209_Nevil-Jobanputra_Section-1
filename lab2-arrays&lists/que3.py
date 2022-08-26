def delatind(l,pos):
    if(pos in range(1,len(l),1)):
        pos = pos-1
        for i in range(pos,len(l)-1,1):
            l[i] = l[i+1]
        
        l.pop(len(l)-1)
        print(l)
    else:
        print("Error!")

l = [1,2,3]
index = 1
print("List after Deletion at Index",index,":")

delatind(l,index)
