import re

def check_password_strength(password):
    
    weak_passwords = [
        "password", "123456", "superman", "test123", "starwars", "iloveyou",
        "sunshine", "monkey", "baseball", "master", "admin123", "dragon",
        "111111", "liverpool"
    ]

    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    has_special = any(char in special_chars for char in password)

    if length and has_upper and has_lower and has_digit and has_special:
        return "Strong: This is a secure password!"
    if length and (has_upper or has_lower) and has_digit:
        return "Moderate: Add special characters for better security."
    if password in weak_passwords or not length:
        return "Weak: Use a longer, less common password."
    
    return "Weak: Improve your password security."

password = input("Enter a password to check its strength: ")
result = check_password_strength(password)

print(result)