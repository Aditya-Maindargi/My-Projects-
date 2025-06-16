import random 
print("  Welcome to the game pls enjoy ")
print('****************************************')


lower_limit = int(input("Enter the lower limit : "))
while True:
    upper_bond = int(input("Enter the upper limit : ")) 
    
    if upper_bond <= lower_limit:
        print("Pls re-enter the number as it is equal or lower than upper bond ")
    else:
        break   

print(f"So your upper bond is {upper_bond} and lower bond is {lower_limit}") 

Guess_number = random.randint(lower_limit, upper_bond)
chances = 5 
Chance_Done = 0
print(f"The number of chances you got is {chances}")

Flag = True 

while Flag:
    while Chance_Done < chances:   # ✅ fixed comparison
        Enter_your_guess = int(input(f"Enter Your Guess No {Chance_Done + 1} : "))
        if Enter_your_guess > Guess_number:
            print("The number is too high, pls guess again ")
            Chance_Done += 1
        elif Enter_your_guess < Guess_number:
            print("The number is lower than the guess number ")
            Chance_Done += 1     # ✅ added missing increment
        else:   # ✅ simplified from `elif Enter_your_guess == Guess_number`
            print("You have guessed the correct number, well done!")
            break
    else:
        print("You have lost all your chances")  # ✅ moved here
    break

print(f"The chances taken by you are {Chance_Done}") 

def reward (Chan):
    if Chan+1 == 1 :
        print("You got 100 ₹ as reward") 
    elif Chan+1 == 2 :
        print("You got 80₹ as reward")
    elif Chan+1 == 3 :
        print("You got 60₹ as reward")
    elif Chan   +1 == 4 :
        print("You got 40₹ as reward") 
    elif Chan   +1 == 5 :
        print("You got 20₹ as reward")
    else:
        print("No reward for you ") 
reward(Chance_Done)