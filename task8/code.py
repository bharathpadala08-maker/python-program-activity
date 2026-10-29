import re

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain at least one special character.")
    if re.search(r"(.)\1{2,}", password):
        errors.append("Password contains excessive character repetition.")
    
    prohibited = ["password", "admin", "1234", "qwerty"]
    for p in prohibited:
        if p in password.lower():
            errors.append(f"Password contains prohibited substring: '{p}'.")
            
    is_valid = len(errors) == 0
    return is_valid, errors

if __name__ == "__main__":
    pwd = "Pass123password!"
    valid, reasons = validate_password(pwd)
    print(f"Password: {pwd}")
    print(f"Valid: {valid}")
    if not valid:
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")
