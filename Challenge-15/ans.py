num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
num3=float(input("enter third number:"))

if num1>=num2 and num1>=num3:
    print(f"{num1} is greatest")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")
