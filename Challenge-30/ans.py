def is_square(num):
    if num<0:
        return false
        
    root=int(num**0.5)
    
    return root*root==num
    
number=int(input("enter a number:"))

if is_square(number):
    print(f"{number} is a perfect square")
else:
    print(f"{number} is not a perfect square")
