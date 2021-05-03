#WAP which accepts marks for four subjects and display total marks , percentage and garde
a=int(input("enter the marks obtained in math:"))
b=int(input("enter the marks obtained in science:"))
c=int(input("enter the marks obtained in engish:"))
d=int(input("enter the marks obtained in computer:"))
total=400
sum=a+b+c+d
print(f"total marks obtained is {sum}")
percentage=(sum/total)*100
print(f"the percentage obtained is {percentage}")
if  percentage <= 40:
    print("you failed")
elif percentage <]



