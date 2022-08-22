weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
elif (unit.upper() == "L"):
    converted = weight * 0.45
    print(f"You are {converted} Lbs")
else:
    print("Invalid input. Press L or K")
