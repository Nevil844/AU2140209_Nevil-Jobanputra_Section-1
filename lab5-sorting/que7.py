import math
import random
def quicksort(arr):
    if(len(arr)<2):
        return arr
    else:
        r=random.randrange(0,len(arr),1)
        pivot=arr[r]

        smaller=list()
        larger=list()

        for i in arr:
            if(i>pivot):
                larger.append(i)
            elif(i<pivot):
                smaller.append(i)
        return quicksort(smaller) + [pivot] + quicksort(larger)

print(quicksort([58,98,-76,682,909]))