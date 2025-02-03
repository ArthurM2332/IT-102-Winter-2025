
def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift  

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount

            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                elif new_char < ord('a'):
                    new_char += 26
            elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                elif new_char < ord('A'):
                    new_char += 26

            result += chr(new_char)
        else:
            result += char

    return result
message = input("Enter your message to encrypt: ")

while True:
    try:
        shift = int(input("Enter the value to shift (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Please enter a valid number 1-25")
    except ValueError:
        print("Invalid input. Please enter an integer between 1-25")

encrypted_message = caesar_cipher(message, shift)
print(f"Encrypted Message: {encrypted_message}")

decrypt_choice = input("Do you want to decrypt? (yes or no): ").strip().lower()
if decrypt_choice in ['yes', 'y']:
    decrypted_message = caesar_cipher(encrypted_message, shift, decrypt=True)
    print(f"Decrypted Message: {decrypted_message}")

