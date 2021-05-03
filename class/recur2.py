def suml(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + suml(l[1:])
l = [2,4,6,8]
a=sum(l)
print(a)