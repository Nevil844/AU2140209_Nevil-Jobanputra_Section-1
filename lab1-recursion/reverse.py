def reverse(s):
    if(len(s[:-1])>0):
        return s[-1]+reverse(s[:-1])
    else:
        return s[-1]

print(reverse("nevil"))