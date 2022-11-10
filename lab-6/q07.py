def chaining(hashTable, keySpace):
    size = len(hashTable)

    for i in keySpace:
        pos = i % size
        hashTable[pos].append(i)

    return hashTable

hashTable = [[],[],[],[],[],[],[],[],[],[]] 
#10 Element 2D Hash Table
keys = [92,123,1993,221,174,333,2112,1133]

hashTable = chaining(hashTable, keys)
print(hashTable)
