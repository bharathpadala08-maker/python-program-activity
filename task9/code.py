import re

def validate_student_record(email, reg_id):
    errors = []
    
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, email):
        errors.append("Invalid email structure or malformed separators.")
    elif not email.endswith("@university.edu"):
        errors.append("Email must belong to the official '@university.edu' domain.")
        
    reg_pattern = r"^\d{2}[A-Z]{3}\d{4}$"
    if not re.match(reg_pattern, reg_id):
        errors.append("Invalid registration identifier format (Expected YYDEPRNNNN).")
        
    is_valid = len(errors) == 0
    return is_valid, errors

if __name__ == "__main__":
    test_email = "john.doe@university.com"
    test_reg_id = "24CS1042"
    
    valid, reasons = validate_student_record(test_email, test_reg_id)
    print(f"Email: {test_email}")
    print(f"Registration ID: {test_reg_id}")
    print(f"Valid: {valid}")
    if not valid:
        print("Errors:")
        for reason in reasons:
            print(f"- {reason}")
