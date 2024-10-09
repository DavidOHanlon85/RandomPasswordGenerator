import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for letter in range(1, nr_letters + 1):
    next_letter = random.choice(letters)
    password += next_letter

for symbol in range(1, nr_symbols + 1):
    next_symbol = random.choice(symbols)
    password += next_symbol

for number in range(1, nr_numbers + 1):
    next_number = random.choice(numbers)
    password += next_number

print(password)

password_before_encryption = list(password)
random.shuffle(password_before_encryption)
password_after_encryption = ''.join(password_before_encryption)

print(f"You're password is {password_after_encryption}")


