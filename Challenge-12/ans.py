def count_vowels(input_string):
    
    vowels="aeiouAEIOU"
    
    count=0
    
    for char in input_string:
       if char in vowels:
          count+=1
    return count

user_input=input("Enter A String:")

vowel_count=count_vowels(user_input)
print(f"The number of vowels in the string is: {vowel_count}")