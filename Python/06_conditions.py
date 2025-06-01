age = int(input("Enter the age: "))

if age <= 0:  
  print("Age cannot negative or zero")
elif age < 18:
  print("Under 18 cannot drive")
else:
  print("You can drive")

# && => and || => or ! => not 

price = 12 if age >= 18 else 8

age = 4

# similar to switch
match age:
  case 1: 
    print("one")
  case 2:
    print("two")
  case _:
    print("Default")