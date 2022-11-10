def hashFunction1(key, s):
    return key % s

def hashFunction2(key, s):
    return s - (key % s)

def doubleHash(hashTable, keyspaces, m, p):
    size = len(hashTable)

    for i in keyspaces:
        probe = 0
        pos = (hashFunction1(i,m) + (probe * hashFunction2(i,p))) % size
        while(hashTable[pos]!=None and pos<size):
            pos = (hashFunction1(i,m) + (probe * hashFunction2(i,p))) % size
            probe = probe + 1
        hashTable[pos] = i

    return(hashTable)

def search(hashTable, lst, m, p):
    size = len(hashTable)
    present = list()

    for i in lst:
        probe = 0
        pos = (hashFunction1(i,m) + (probe * hashFunction2(i,p))) % size
        while(hashTable[pos]!=None and pos<size):
            if(hashTable[pos]==i):
                present.append(True)
                break
            probe = probe + 1
            pos = (hashFunction1(i,m) + (probe * hashFunction2(i,p))) % size
        else:
            present.append(False)

    return(present)

hashTable1 = [None]*17
keySpace = [133,88,92,221,174]

hashTable1 = doubleHash(hashTable1, keySpace, 17,11)
searchFor = [100,133,174]

print("Hash Table 1:")
print(hashTable1)

p1 = search(hashTable1, searchFor, 17, 11)
for i in range(len(p1)):
    if(p1[i]):
        print(searchFor[i],"is Present.")
    else:
        print(searchFor[i],"is NOT Present.")