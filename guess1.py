
import random as r

number = r.randint(1,17)
print(number)
chance = 0
while chance < 8:
    guess = input("Enter the guessng number: ")
    if not guess.isdigit():
        print("enter valid number!!")
        continue
    guess = int(guess)

    if guess >= 50:
        print("Too High")
        break
    
   
    if guess == number:
            print("Congratulations! You guessed it!")
          
            break
    else:
        print("not correct, Try again!!")
        chance = chance + 1
        
if chance > 7:
    print(f"OVER! The correct number was {number}")
