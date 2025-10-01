import random


compNumber = random.randint(1,100)

def ask():
    user = int(input("Guess the number: "))
    return user


user = ask()


while user != compNumber:
    if user > compNumber:
        print("Your number is greater then computer guessed number")
        user = ask()
    else:
        print("Your number is smaller then computer guessed number")
        user = ask()
    


print("Congratulation, You guessed the right number")    