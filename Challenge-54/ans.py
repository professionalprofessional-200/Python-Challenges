def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example usage
nums1 = [1, 2, 3, 4, 10]
nums2 = [5, 3, 2, 1]

print("Is nums1 sorted?", is_sorted(nums1))  # True
print("Is nums2 sorted?", is_sorted(nums2))  # False
