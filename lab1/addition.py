#if name is less than three character long name must be at least 3 character otherwise if its more than 50 character name must be maximum of 50 cahracters otherwise name looks good
name=input("enter your name")
if len(name)<3:
    print("name must be atleast three character")
elif len(name)<50:
    print("name must be less than 50")
else:
    print("thank you")

