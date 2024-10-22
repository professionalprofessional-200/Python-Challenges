number=int(input("Enter a number:"))

print(f"\nMultiplication of {number} is:")

for i in range(1,21):
    result=i*number
    print(f"{i}*{number}={result}")
