import random

random_number = random.randrange(0, 10)
count = 0


while True:
    number = int(input("Guess a number between 0 and 10: "))
    count +=1

    if number == random_number:
        print("You guessed right.")
        print("You guessed " + str(count) + " times")
        break

    if number < random_number:
        print("Your number is too small. Guess again.")

    if number > random_number:
        print("Your number is too big. Guess again.")

