def isPali(x):
  if(len(x)>1):
    if(x[0]==x[-1]):
      isPali(x[1:-1])
    if(x[0]!=x[-1]):
      print("Not a palindrome")
  else:
    print("Palindrome")
        
word=input()
x=[i for i in word]
isPali(x)