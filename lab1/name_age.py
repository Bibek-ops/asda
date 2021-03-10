weight=int(input("enter weight="))
unit=input("(l)bs or k(g):")
if unit.upper()=="l":
    converted_lbs=weight=0.45
    print(f"the person weight is {converted_lbs} kilos")
elif unit.upper()=="k":
    converted_kg= weight/o.45
    print(f"the person weight is {converted_kg} pounds")
else:
    print(f"please enter appropriate character as K for kg or L for lbs!!")


