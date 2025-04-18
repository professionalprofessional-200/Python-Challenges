from collections import Counter

try:
    with open("today topics(py).txt", "r") as file:
        text = file.read().lower()  # Read all text and convert to lowercase
        words = text.split()        # Split text into words
        word_count = Counter(words) # Count frequency using Counter

        for word, count in word_count.items():
            print(f"{word}: {count}")

except FileNotFoundError:
    print("The file was not found.")
