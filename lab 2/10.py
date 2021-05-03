#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
a=int(input("enter a integer:"))
b=int(input("enter a integer:"))
c=int(input("enter a integer :"))
e=a+b+c
if a==b or b==c or c==a:
    print("zero")
else:
    print(e)





