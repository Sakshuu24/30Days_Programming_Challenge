# Day 2 Solution: Find the Missing Number
# Date: 16-Aug-2025

from problem import find_missing_number

def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = total_sum - actual_sum
    return missing_number

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 4, 5]  # Example array
    print("Array:", arr)
    print("Missing number:", find_missing_number(arr))
