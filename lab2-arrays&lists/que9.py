def replatind(ar,p,e):
    if p <= (len(ar)):
        ar[p-1]=e
        print(ar)
    else:
        print("-1")

l1 = [1,2,3,4]

print("Example of Valid Input : ")
replatind(l1,2,6)
print("\nExample of Invalid Input : ")
replatind(l1,10,5)