def is_alphabetic(string):
    return string.isalpha()
    
user_input=input("enter your input:")

if is_alphabetic(user_input):
    print("Your input contain alphabetic letters only")
    
else:
    print("Your input contain does not have alphabetic letters only")
