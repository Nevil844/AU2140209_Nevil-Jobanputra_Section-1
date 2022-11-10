def BloomFilter(ht17, ht37, keySpace):
    for i in keySpace:
        pos1 = i % 17
        pos2 = i % 37

        ht17[pos1] = 1
        ht37[pos2] = 1


def search(ht17, ht37, lst, keySpace):
    for i in lst:
        a = ht17[i % 17] == 1
        b = ht37[i % 37] == 1

        if(a and b):
            print(i,"is present according to Bloom Filter.")
            if(i in keySpace):
                print(i,"is also present actually.")
            else:
                print("But it is not present really.")
        
        else:
            print(i,"is not present.\n")

hash17 = [0]*17
hash37 = [0]*37

keySP = [133,88,92,221,174]
searchFor = [100,133,174]

BloomFilter(hash17, hash37, keySP)
search(hash17, hash37, searchFor, keySP)