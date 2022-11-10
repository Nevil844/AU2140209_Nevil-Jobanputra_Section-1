def polynomialHash(hashTable,string):
    a = 2 
    summ = 0

    for i in range(len(string)):
        summ = summ + (ord(string[i])*(a**i))

    return summ

hashTable = [None]*32

print("fist")
print("Polynomial Hash Value:",polynomialHash(hashTable, "fist"))
print("Hash Value Modulo 17:",(polynomialHash(hashTable, "fist"))%17)
print("Hash Value Modulo 37:",(polynomialHash(hashTable, "fist"))%37)
print()

print("sift")
print("Polynomial Hash Value:",polynomialHash(hashTable, "sift"))
print("Hash Value Modulo 17:",(polynomialHash(hashTable, "sift"))%17)
print("Hash Value Modulo 37:",(polynomialHash(hashTable, "sift"))%37)
print()

print("shift")
print("Polynomial Hash Value:",polynomialHash(hashTable, "shift"))
print("Hash Value Modulo 17:",(polynomialHash(hashTable, "shift"))%17)
print("Hash Value Modulo 37:",(polynomialHash(hashTable, "shift"))%37)
print()

print("fast")
print("Polynomial Hash Value:",polynomialHash(hashTable, "fast"))
print("Hash Value Modulo 17:",(polynomialHash(hashTable, "fast"))%17)
print("Hash Value Modulo 37:",(polynomialHash(hashTable, "fast"))%37)
print()

print("faster")
print("Polynomial Hash Value:",polynomialHash(hashTable, "faster"))
print("Hash Value Modulo 17:",(polynomialHash(hashTable, "faster"))%17)
print("Hash Value Modulo 37:",(polynomialHash(hashTable, "faster"))%37)
print()

print("shaft")
print("Polynomial Hash Value:",polynomialHash(hashTable, "shaft"))
print("Hash Value Modulo 17:",(polynomialHash(hashTable, "shaft"))%17)
print("Hash Value Modulo 37:",(polynomialHash(hashTable, "shaft"))%37)
print()