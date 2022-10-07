def mergesort(l1,l2):

    lst=list()
    m=len(l1)+len(l2)
    while(len(lst)!=m):
        if(len(l1)==0):
            lst.extend(l2)
        elif(len(l2)==0):
            lst.extend(l1)
        elif(l1[0]<l2[0]):
            lst.append(l1[0])
            l1.pop(0)
        elif(l2[0]<l1[0]):
            lst.append(l2[0])
            l2.pop(0)
        else:
            lst.append(l1[0],l2[0])
            l1.pop(0)
            l2.pop(0)
    return lst

def divide(arr):
    if(len(arr)==1):
        return arr
    else:
        a=divide(arr[:len(arr)//2])
        b=divide(arr[len(arr)//2:])
        return mergesort(a,b)


print(divide([112,35,-63,24,46,-99]))
print(mergesort([45,22,16],[75,245,678]))