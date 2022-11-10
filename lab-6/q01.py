def linearProbe(hashTable, keys):
    size = len(hashTable)

    for i in keys:
        index = 0
        pos = (i+index) % size
        while(hashTable[pos]!=None):
            pos = (i+index) % size
            index = index + 1
        hashTable[pos] = i

    return(hashTable)

def search(hashTable, lst):
    size = len(hashTable)
    present = list()

    for i in lst:
        index = 0
        pos = (i+index) % size
        while(hashTable[pos]!=None):
            if(hashTable[pos]==i):
                present.append(True)
                break
            index = index + 1
            pos = (i+index) % size
        else:
            present.append(False)

    return(present)

hashTable1 = [None]*17
hashTable2 = [None]*37

keySpace = [133,88,92,221,174]

hashTable1 = linearProbe(hashTable1, keySpace)
hashTable2 = linearProbe(hashTable2, keySpace)

searchFor = [100,133,174]

print("Hashtable 1 :")
print(hashTable1)
print()
print("Search for:")
print(searchFor)

p1 = search(hashTable1, searchFor)
for i in range(len(p1)):
    if(p1[i]):
        print(searchFor[i],"is Present.")
    else:
        print(searchFor[i],"is NOT Present.")

print("Hashtable 2:")
print(hashTable2)
print("Search for:")
print(searchFor)

p2 = search(hashTable2, searchFor)
for i in range(len(p2)):
    if(p2[i]):
        print(searchFor[i],"is Present.")
    else:
        print(searchFor[i],"is NOT Present.")