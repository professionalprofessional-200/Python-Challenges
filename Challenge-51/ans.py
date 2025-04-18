def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Each element is at least an LIS of length 1

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:  # Increasing condition
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if arr else 0

# Example usage
nums = [10, 22, 9, 33, 21, 50, 41, 60]
length = longest_increasing_subsequence(nums)
print("Length of Longest Increasing Subsequence is:", length)
