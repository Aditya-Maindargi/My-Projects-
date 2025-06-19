import random

print("Lets Play Stone ✊ Paper ✋ Scissors ✌️") 

User_points = 0 
Comp_points = 0
choice_bucket = ["Stone", "Paper", "Scissor"]

def Game(user, User_score, Comp_score):
    print(f"So your choice is {user} right") 
    print("Now computers turn ")
    
    Computer = random.choice(choice_bucket) 
    print(f"So computer choice is {Computer}") 
    print(f"Now its {Computer} V/S {user}  ") 

    if Computer == user:
        print("==>DRAW<==") 
        Comp_score += 0.5 
        User_score += 0.5 
    elif Computer == "Stone" and user == "Paper":
        print("User is the winner ")
        User_score += 1
    elif Computer == "Paper" and user == "Scissor":
        print("User is the winner ") 
        User_score += 1
    elif Computer == "Scissor" and user == "Stone":
        print("User is the winner ") 
        User_score += 1
    else: 
        print("The computer is winner")
        Comp_score += 1 

    print(f"Yur points are {User_score} and computer points are {Comp_score} .")
    return User_score, Comp_score

# main game loop
while True:
    Play_again = input("Do you want to play? (Yes/No): ").lower().strip()
    if Play_again not in ["yes", "y"]:
        break

    while True:
        user_choice = input("Enter What you want to play Stone/Paper/Scissor : ").capitalize().strip()
        if user_choice in choice_bucket:
            break
        print("Please enter your choice correctly.")

    User_points, Comp_points = Game(user_choice, User_points, Comp_points)

# final winner after quitting
print("\nThe final winner is:")
if User_points > Comp_points:
    print("User 👤")
elif User_points < Comp_points:
    print("Computer 💻")
else:
    print("It's a tie! 🤝")
