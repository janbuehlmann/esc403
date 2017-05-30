min = 1
max = 100

while True:
   computer_guess = int((min + max)/2)
   print("My guess is: " + str(computer_guess))
   user_input = input("Is this correct? ")

   if user_input == "=":
       print("Hooray, I have won :_)")
       break

   elif user_input == "<":
       max = computer_guess - 1

   elif user_input == ">":
       min = computer_guess + 1
