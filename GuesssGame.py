
import random as r
print("This iS Guessing Game, Enter Number Between 1-15, You have 7 chances.. Good Luck  \n ")
number = r.randint(1,15)


chance = 0
while chance < 3:
    guess = input("Enter the guessng number: ")
    if not guess.isdigit():
        print("enter valid number!!")
        continue
    guess = int(guess)

    if guess > 15:
        print("Too High, Are You Kidding Me!!")
        
    if guess < number -5:
        print("too low,try higher")
        
    if guess > number +5 :
        print("too high,try lower")
        
    if guess == number:
            print("Congratulations! You guessed it!")
          
            break
    else:
        print("not correct, Try again!!")
        chance = chance + 1
        
if chance > 7:
    print(f"OVER! The correct number was {number}")
