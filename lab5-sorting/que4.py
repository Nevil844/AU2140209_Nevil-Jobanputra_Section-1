import time


def binarySearch(arr, ele, s, e): 
    if e - s <2:
        if(arr[ele]<arr[s]):
            y = s-1
            return y
        else:
            return s
    mid = (s+e)//2

    if(arr[mid] > arr[ele]):
        return binarySearch(arr,ele,s,mid)

    elif(arr[mid] < arr[ele]):
        return binarySearch(arr,ele,mid,e)

    else:
        return mid 

def insertionsortBinary(arr):
    for i in range(1,len(arr)):
        tmp = arr[i] 
        z =  binarySearch(arr,i,0,i)
        pos = z + 1
        for j in range(i,pos,-1):
            arr[j] = arr[j-1]
        arr[pos] = tmp
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

def selectionSort(arr):
    for i in range(len(arr)-1):
        min = i
        count = 0
        for j in range(i,(len(arr))):
            if arr[min] > arr[j]:
                min = j
                count += 1

        tmp = arr[min]
        arr[min] = arr[i]
        arr[i] = tmp
    return arr 



worstCase = list(map(int, input("Enter values for worst case : ").split()))
bestCase = list(map(int, input("Enter values for best case : ").split()))

w = insertionsortBinary(worstCase)
timebiWorst = time.perf_counter()
b = insertionsortBinary(bestCase)
timebiBest = time.perf_counter()
print("\nUnsorted array(Worst case) : ",worstCase)
print("\nSorted array(best case) : ",bestCase)
print("\nSorted array using Binary_insertionsort: ",w," \nTime(Worst) : ",timebiWorst," Time(Best) :",timebiBest)
w = insertionsortLinear(worstCase)
timeliWorst = time.perf_counter()
b = insertionsortLinear(bestCase)
timeliBest = time.perf_counter()
print("\nSorted array using Linear_insertionsort: ",w," \nTime(Worst) : ",timeliWorst," Time(Best) :",timeliBest)
w = selectionSort(worstCase)
timessWorst = time.perf_counter()
b = selectionSort(bestCase)
timessBest = time.perf_counter()
print("\nSorted  array  using  selection  sort  : ",w," \nTime(Worst) : ",timessWorst," Time(Best) :",timessBest)
