#for find sum value of list

x=sum([11,12,31,14,51])

print(x)

#user friendly way

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

total_sum = sum(numbers)

print(f"The sum of the numbers is: {total_sum}")

