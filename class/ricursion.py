def mil(n):
    if n==2:
        return 3
    else:
        return 3+mil(n-1)
a=mil(3)
print(a)



