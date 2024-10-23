def longest_word(sentence):
    
    words = sentence.split()
    
    if not words:  
        return "", 0  
    longest = max(words, key=len)  
    longest_length = len(longest) 

    return longest, longest_length

user_input = input("Enter a sentence: ")

longest_word_result, length = longest_word(user_input)

print("The longest word is:", longest_word_result)
print("The length of the longest word is:", length)
