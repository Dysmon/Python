import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

quantity = int(input("Number of passwords to generate: "))
length = int(input("Length of password: "))
if input("include numbers?(y/n)\n").lower().strip() == 'y':
    chars += digits
if input("include lowercase_letters?(y/n)\n").lower().strip() == 'y':
    chars += lowercase_letters
if input("include uppercase_letters?(y/n)\n").lower().strip() == 'y':
    chars += uppercase_letters
if input("include punctuation?(y/n)\n").lower().strip() == 'y':
    chars += punctuation
if input("exclude ambiguous characters 'il1Lo0O?'\n").lower().strip() == 'y':
    for ch in "il1Lo0O?":
        chars = chars.replace(ch, "")

def generate_password(chars, length):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

if chars != "":
    for _ in range(quantity):
        print(generate_password(chars, length))
