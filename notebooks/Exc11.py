import random


number = int(input("Give a number between 0 and 10: "))
computer_guess = random.randrange(0, 10)

count = 0


while True:
    count +=1

    if number == computer_guess:
        print("The computer guessed right.")
        print("He had to guess computer " + str(count) + " times")
        break

    elif number < computer_guess:
        print("The computer guessed " + computer_guess)
        hint = input("Give the computer a hint by inserting < or >: ")
        computer_guess = random.randrange(0, computer_guess)

    elif number > computer_guess:
        print(computer_guess)
        hint = input("Give the computer a hint by inserting < or >: ")
        computer_guess = random.randrange(computer_guess, 10)