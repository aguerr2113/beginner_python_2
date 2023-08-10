import string
import secrets

def contains_upper(password):
    for char in password:
        if char.isupper():
            return True
        
    return False
def contains_symbols(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length,symbols,uppercase):
    combination = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    new_password = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password
if __name__ == '__main__':
    for i in  range(1,6):
        new_passw = generate_password(length=10,symbols=False,uppercase=False)
        specs = f'U: {contains_upper(new_passw)}, S: {contains_symbols(new_passw)}'
        print(f'{i} -> {new_passw} ({specs})')