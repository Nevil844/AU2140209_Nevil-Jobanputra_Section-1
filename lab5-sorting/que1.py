def bubblesort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
                
    print(arr)
    
x=list(map(int, input("Enter values: ").split()))
    
bubblesort(x)