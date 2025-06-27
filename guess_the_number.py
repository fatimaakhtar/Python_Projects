import random

target = random.randint(1,100)
while True:
    guess = (input("Enter your guess or quit(q): "))
    if guess =="q":
        break
    guess = int(guess)
    if guess == target:
        print("Hurrah! You guessed it!")
        break

    elif guess > target:
        print("Your guess is high. Guess a smaller number.")
    else:
        print("Your guess is low. Guess a larger number.")


print("---GAME OVER---")