import time

def countsort(array,p):
    st = len(array)
    rs = [0] * st
    fns = [0] * 10
    for i in range(0, st):
        index = array[i] // p
        fns[index % 10] += 1
        
    for i in range(1, 10):
        fns[i] += fns[i - 1]

    i = st - 1
    while i >= 0:
        index = array[i] // p  
        rs[fns[index % 10] - 1] = array[i]
        fns[index % 10] -= 1
        i -= 1
        
    for i in range(0, st):
        array[i] = rs[i]

def radixsort(array):
    maxArr = max(array)

    pos = 1
    while maxArr // pos > 0:
        countsort(array, pos)
        pos *= 10

    return array

x=list(map(int, input("Enter values: ").split()))
x = radixsort(x)
timeRadixsort = time.perf_counter()

print("\n Sorted array : ",x," Time : ",timeRadixsort)