#how many hours and minutes are displayed on the 24h digital clock
n=int(input("enter time in minutes :"))
hours=(n//60)
minutes=(n%60)
print(f"the hour is {hours}")
print(f"the minute is{minutes}")
print(f"its {hours}:{minutes} now")


