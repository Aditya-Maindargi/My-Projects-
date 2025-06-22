import random

# Find nearest multiple of 4
def nearestMultiple(num):
    return num + (4 - num % 4) if num >= 4 else 4

# Check if list has only consecutive numbers
def check(xyz):
    return all(xyz[i] - xyz[i - 1] == 1 for i in range(1, len(xyz)))

# If player loses
def lose1():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

# If player wins
def win1():
    print("\n\nCONGRATULATIONS !!!")
    print("YOU WON!")
    exit(0)

# Game starts here
def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ').strip().upper()

        if chance == "F":
            while True:
                if last == 20:
                    lose1()

                print("\nYour Turn.")
                while True:
                    try:
                        inp = int(input("How many numbers do you want to say (1–3)?\n> "))
                        if 1 <= inp <= 3:
                            break
                        else:
                            print("Enter only 1, 2, or 3.")
                    except:
                        print("Enter a valid number.")

                comp = 4 - inp
                print("Now your numbers are:")
                for _ in range(inp):
                    last += 1
                    xyz.append(last)
                    print(last, end=" ")
                    if last == 21:
                        print("\nYou said 21!")
                        lose1()
                print("\n")

                print("Computer's turn:")
                for _ in range(comp):
                    last += 1
                    xyz.append(last)
                    print(last, end=" ")
                    if last == 21:
                        print("\nComputer said 21!")
                        win1()
                print("\nOrder of inputs so far:", xyz)

        elif chance == "S":
            comp = 1
            while last < 21:
                print("Computer's turn:")
                for _ in range(comp):
                    last += 1
                    xyz.append(last)
                    print(last, end=" ")
                    if last == 21:
                        print("\nComputer said 21!")
                        win1()
                print("\nOrder of inputs so far:", xyz)

                if last >= 21:
                    lose1()

                print("\nYour Turn.")
                while True:
                    try:
                        inp = int(input("How many numbers do you want to say (1–3)?\n> "))
                        if 1 <= inp <= 3:
                            break
                        else:
                            print("Enter only 1, 2, or 3.")
                    except:
                        print("Enter a valid number.")

                print("Now your numbers are:")
                for _ in range(inp):
                    last += 1
                    xyz.append(last)
                    print(last, end=" ")
                    if last == 21:
                        print("\nYou said 21!")
                        lose1()
                print()

                near = nearestMultiple(last)
                comp = near - last if near - last <= 3 else 3

        else:
            print("Wrong choice. Please enter 'F' or 'S'.")

# Main loop
while True:
    print("\nPlayer 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ').strip().lower()

    if ans == 'yes':
        start1()
    elif ans == 'no':
        print("Do you want to quit the game? (yes / no)")
        nex = input('> ').strip().lower()
        if nex == "yes":
            print("You are quitting the game...")
            exit(0)
        elif nex == "no":
            print("Continuing...\n")
        else:
            print("Wrong choice.\n")
    else:
        print("Invalid input.\n")
