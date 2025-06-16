import random as ran

print("Hello to my \n** Physics Term Guess Game **\n")
print("************************************")


# For asking the name
def name(Name):
    print(f"So {Name}, all the best for the game.")
    print("Let's go!")


def Game(Word_random):
    no_of_chance = 10
    guessed_letters = ""
    
    while no_of_chance > 0:
        failed = 0
        for char in Word_random:
            if char.lower() in guessed_letters:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        
        print()
        
        if failed == 0:
            print("You win!")
            print(f"The word was: {Word_random}")
            break
        
        guess = input("Guess a letter: ").lower()
        guessed_letters += guess
        
        if guess not in Word_random.lower():
            no_of_chance -= 1
            print("Wrong guess.")
            print(f"Remaining chances: {no_of_chance}")
            
            if no_of_chance == 0:
                print("You lost!")
                print(f"The word was: {Word_random}")


# Main game logic
NAME = input("Enter your name please: ")
word_bank = ["Vector", "Velocity", "Angle", "Newton", "Tesla", "Electron", "Acceleration", "Volt", "Hertz", "Meters"]
word_to_be_guessed = ran.choice(word_bank)

name(NAME)
Game(word_to_be_guessed)



#65% of the code was done by me 
