def find_gcd(a,b):
    while b != 0:
      a,b = b,a%b
    return a
    
a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))

gcd=find_gcd(a,b)

print(f"GCD for given number is : {gcd}")
