numbers=input("numbers are separated by spaces:")

number_list=[float(num) for num in numbers.split()]

total_sum=0

for number in number_list:
    total_sum += number
    
print(f"The sum of all number is : {total_sum}")
