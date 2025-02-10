import random
import string
def get_password_criteria():
    while True:
        try:
            length = int(input("Enter password length (minimum 8 characters): "))
            if length < 8:
                print("Password must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    include_uppercase = input("Include uppercase letters (y/n): ").strip().lower() == 'y'
    include_lowercase = input("Include lowercase letters (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers (y/n): ").strip().lower() == 'y'
    include_specials = input("Include special characters (y/n): ").strip().lower() == 'y'

    if not (include_uppercase or include_lowercase or include_numbers or include_specials):
        print("You must select at least one character type.")
        return get_password_criteria()

    return length, include_uppercase, include_lowercase, include_specials, include_numbers

def generate_password(length, include_uppercase, include_lowercase, include_specials, include_numbers):
    char_sets = ""
    guaranteed_chars = []

    if include_uppercase:
        char_sets += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))

    if include_lowercase:
        char_sets += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))

    if include_numbers:
        char_sets += string.digits
        guaranteed_chars.append(random.choice(string.digits))

    if include_specials:
        char_sets += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars + random.choices(char_sets, k=remaining_length)
    random.shuffle(password_chars)

    return ''.join(password_chars)


def main():
    while True:
        length, uppercase, lowercase, numbers, specials = get_password_criteria()
        password = generate_password(length, uppercase, lowercase, specials, numbers)
        print(f"\nGenerated password: {password}\n")

        retry = input("Generate another password (y/n): ").strip().lower()
        if retry != 'y':
            print("Goodbye!")
            break


main()
