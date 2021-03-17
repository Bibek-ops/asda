secret=8
attempt=0
while (attempt < 3):
    inp =int(input("enter  a number:"))
    if inp== secret:
        print("you are right")
        break
    else:
        attempt+=1
        print("try again")
    print("you failed")
