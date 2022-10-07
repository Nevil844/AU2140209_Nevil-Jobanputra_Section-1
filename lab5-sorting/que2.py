def bubblesort(arr):
    for i in range(0,len(arr)-1):
        x=i
        for j in range(i+1,len(arr)):
            if(arr[x]>arr[j]):
                x=j
    
        tmp = arr[x]
        arr[x]=arr[i]
        arr[i]=tmp
            
    print(arr)

x=list(map(int, input("Enter values: ").split()))
    
bubblesort(x)