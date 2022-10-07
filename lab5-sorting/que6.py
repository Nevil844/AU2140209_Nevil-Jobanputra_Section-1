def quicksort(arr):
    if(len(arr)<2):
        return arr
    else:
        pivot=arr[len(arr)//2]

        smaller=list()
        larger=list()

        for i in arr:
            if(i>pivot):
                larger.append(i)
            elif(i<pivot):
                smaller.append(i)
        return quicksort(smaller) + [pivot] + quicksort(larger)

print(quicksort([58,98,-76,682,909]))