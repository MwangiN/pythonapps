import random

def guess(x): #function definition
    random_number = random.randint(1,x) #returns a random number for us to guess
    guess = 0 #ensure guess should not be equal to zero
    while guess!= random_number:
        guess=int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number:
            print("Sorry,try again.Too Low")
        elif guess > random_number:
             print("Sorry, try again.Too High")

    print(f"Congratulations, your guess was right {random_number}")  

guess(50)

