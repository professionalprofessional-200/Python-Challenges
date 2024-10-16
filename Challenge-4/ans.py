#we can solve this problem in two methods
#for loop method
n=int(input("Enter number:"))
factorial=1
for i in range(1,n+1):
      factorial*=i
      
print(f"The {n} factorial is {factorial}")

#while loop method
n = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"The factorial of {n} is {factorial}")
