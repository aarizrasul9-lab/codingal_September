print("Select a ride")
print("1. Bike")
print("2. Car")
print("3. Roller Coaster")

choice = int(input("Enter your choice: "))

if( choice == 1 ):
    print("what type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")
    print("3. Roller Skates\n")

    choice2=int(input("Enter your Choice2: "))
    if choice2==1:
        print("You have selected a scooty")
    else:
        print("You have selected a Scotter")
        

elif( choice == 2 ):
    print("what type of car?")
    print("1. Serdan\n")
    print("2. SUV\n")
    print("3. BMW\n")

    choice3=int(input("Enter your choice3: "))
    if choice3==1:
        print("You have Selected a Serdan")
    else:
        print("You have selected a SUV")
else:
    print("Wrong Choice!")