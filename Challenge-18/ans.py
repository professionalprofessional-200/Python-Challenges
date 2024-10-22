def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    if b==0:
        print("error")
    else:
        return a/b
    
print("select operation:")
print("1.Addtion")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

number=int(input("Enter Your Option:"))

num1=float(input("Enter your 1st number:"))
num2=float(input("Enter your 2nd number:"))

if number==1:
    print(f"Addition:{add(num1,num2)}")

elif number==2:
    print(f"Substraction:{sub(num1,num2)}")
    
elif number==3:
    print(f"Multiplication:{mul(num1,num2)}")
    
else:
    print(f"Division:{div(num1,num2)}")
