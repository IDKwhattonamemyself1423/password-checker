import re

def check_password_strength(password):
    # length check
    if len(password) < 12:
        return "weak password, make it longer"
    # uppercase check
    if not re.search(r'[A-Z]', password):
        return "weak password, put at least 1 uppercase letter, bruh"
    # lowercase check
    if not re.search(r'[a-z]', password):
        return "weak password, put at least 1 lowercase letter, bruh"
    # number check
    if not re.search(r'[0-9]', password):
        return "weak password, put at least 1 number, bruh"
    # special character
    if not re.search(r'[!@#$%^&*()-]', password):
        return "weak password, put at least 1 special character, bruh"

    return "strong password, bruh"

while True:
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
    if result == "strong password, bruh":
        break
