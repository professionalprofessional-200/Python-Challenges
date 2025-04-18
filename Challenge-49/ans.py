def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        result.append(new_row)

    return result

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = transpose(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
