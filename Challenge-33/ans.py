def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:", result)
