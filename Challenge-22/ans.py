numbers=input("Numbers are separated by spaces:")
number_list=[int(num) for num in numbers.split()]

unique_numbers=[]
for num in number_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
        
print(f"List:{unique_numbers}")
