def validate_password(password):
    
    # Checking the length of the password
    if len(password) < 8:
        return False
    
    # Checking for uppercase, lowercase, and digit presence
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
    
    if not (has_uppercase and has_lowercase and has_digit):
        return False
    
    # Checking for spaces in the password
    if ' ' in password:
        return False
    
    return True