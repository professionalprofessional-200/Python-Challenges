def second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two numbers."

    unique_numbers = list(set(numbers))  # Remove duplicates

    if len(unique_numbers) < 2:
        return "All numbers are the same."

    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1]           # Second largest is at index 1

# Example usage
nums = [10, 20, 4, 45, 99, 99]
print("Second largest number is:", second_largest(nums))
