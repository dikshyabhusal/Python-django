#Wap to take user input email and validate wheather it is corrent email or not

email = input("Enter your email: ")

def validate_email(email):
    if email.count('@') != 1:
        return False
    
    first_part, domain_part = email.split('@')

    if domain_part.count('.') != 1:
        return False
    
    domain_name, extension = domain_part.split('.')
    
    if not (first_part.isalpha() and domain_name.isalpha() and extension.isalpha()):
        return False
    
    return True

if validate_email(email):
    print("The email is valid.")
else:
    print("The email is not valid. It should not contain any numbers or special characters.")
