import re
import sys
import random
import string

def length_checker(password):
    length = len(password)
    if length < 12:
        print("📌Your password is " + str(length) + " characters long. We recommend using at least 12 characters long passwords.")
        return 0
    else:
        print("📌Password length ✅")
        return 1

def special_character_checker(password):
    pattern = r'[!@#$%^&*(),.?":{}|<>]'
    if bool(re.search(pattern, password)):
        print("📌Special character ✅")
        return 1
    else:
        print("📌Your password doesn't contain special characters. We recommend using at least one special character.")
        return 0

def uppercase_character_checker(password):
    pattern = r'[A-Z]'
    if bool(re.search(pattern, password)):
        print("📌Uppercase character ✅")
        return 1
    else:
        print("📌Your password doesn't contain uppercase characters. We recommend using at least one uppercase character.")
        return 0

def lowercase_character_checker(password):
    pattern = r'[a-z]'
    if bool(re.search(pattern, password)):
        print("📌Lowercase characters ✅")
        return 1
    else:
        print("📌Your password doesn't contain lowercase characters. We recommend using at least one lowercase character.")
        return 0

def number_checker(password):
    if any(char.isdigit() for char in password):
        print("📌Number ✅")
        return 1
    else:
        print("📌Your password doesn't contain numbers. We recommend using at least one number.")
        return 0

def common_passwords(password):
    common = ["123456", "123456789", "qwerty", "password", "12345", "qwerty123", "admin"]
    if password in common:
        print("🥱 This is one of the most commonly used passwords. Be creative.")
        sys.exit()

def recommendation(password, length, special, upper, lower, number):
    if length + special + upper + lower + number == 5:
        print("Your Password is Perfectly strong 💪")
    else:
        additions = []
        
        if length == 0:
            additions.extend(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12-len(password)))
        
        if special == 0:
            additions.append(random.choice(string.punctuation))
        
        if upper == 0:
            additions.append(random.choice(string.ascii_uppercase))
        
        if lower == 0:
            additions.append(random.choice(string.ascii_lowercase))
        
        if number == 0:
            additions.append(random.choice(string.digits))
        
        new_password = list(password) + additions
       
        new_password = ''.join(new_password)
        print("Here is your corrected password: " + new_password)

print("This program will check if your password is strong or not based on the following criteria:")
print("1: Presence of uppercase and lowercase letters")
print("2: Presence of special characters")
print("3: Length of the password")
print("4: Comparison with commonly used passwords")

password = input("Enter your password: ")
print("Process is complete and here are our findings:")
common_passwords(password)
length = int(length_checker(password))
special = int(special_character_checker(password))
upper = int(uppercase_character_checker(password))
lower = int(lowercase_character_checker(password))
number = int(number_checker(password))
recommendation(password, length, special, upper, lower, number)

