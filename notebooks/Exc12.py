import json
address_book_file = ("address_book.txt", "r")
address_book = json.load(address_book_file)
address_book_file.close

while True:
    name = str(input("What's your name honey? "))
    phone = int(input("Now give me your phone number, sugar: "))
    if name == "exit":
        break
    phone = int(input("Now give me your phone number, sugar: "))
    address_book[name] = number

    elif name != str("exit"):
        file.write(name\n')
        file.write(phone\n')

address_book_file = ("address_book.txt", "")
address_book_file.write(json.dumps(address_book))
address_book_file.close()








