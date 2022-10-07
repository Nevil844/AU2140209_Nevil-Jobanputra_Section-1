from re import X
import time


def binarySearch(arr,ele,s,e): 
    if e-s <=1:
        if(arr[ele]<arr[s]):
            x = s-1
            return x
        else:
            return s
    mid = (s + e) // 2

    if(arr[mid] > arr[ele]):
        return binarySearch(arr,ele,s,mid)

    elif(arr[mid] < arr[ele]):
        return binarySearch(arr,ele,mid,e)

    else:
        return mid 

def insertionsortBinary(arr):
    n = len(arr)
    for i in range(1,n):
        tmp = arr[i] 
        t = binarySearch(arr,i,0,i)
        position = t + 1
        for j in range(i,position,-1):
            arr[j] = arr[j-1]
        arr[position] = tmp
    return arr 

def insertionsortLinear(arr):
    for i in range(1,len(arr)):
        tmp = arr[i]
        j = i
        while tmp <= arr[j-1] and j > 0 :
            arr[j] = arr[j-1]
            j -=1
        arr[j] = tmp
    return arr



y=list(map(int, input("Enter values: ").split()))
y = insertionsortBinary(y)
timebi = time.perf_counter()
print("\nUnsorted array : ",y)
print("\nSorted array using Binary : ",y," Time : ",timebi)
y = insertionsortLinear(y)
timeli = time.perf_counter()
print("\nSorted array using linear : ",y," Time : ",timeli)
