#given a three digit number find the sum its digits
number=int(input("enter a three digit number"))
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)