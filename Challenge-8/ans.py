def is_palindrome(s):
  # Convert the string to lowercase to ignore case sensitivity
    s = s.lower()
    
    return s[::-1]

user_string = input("Enter a string: ")

if is_palindrome(user_string):
    print(f"'{user_string}' is palindrome")
else:
    print(f"'{user_string}' is palindrome")
