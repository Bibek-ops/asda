def a(num):
    for i in range(1,11):
        product=num*i
        print(f"{num}*{i}={product}")
num=int(input("enter number for multiplication table:"))
a(num)