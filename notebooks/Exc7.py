# - Write a function print_reverse(text) which expects a string as an
#  argument and prints every character of the string in reverse order
# - Use a while loop to do this




def print_reverse(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    print(new_string)

print_reverse("no lemon, no melon")
