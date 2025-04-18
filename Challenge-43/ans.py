# Make sure there's a file named 'sample.txt' in the same directory
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes the extra newline character
except FileNotFoundError:
    print("The file was not found.")
