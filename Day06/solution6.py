def find_subarrays_with_zero_sum(arr):
    """
    Function to find all subarrays with zero sum.

    Args:
        arr (list): List of integers.

    Returns:
        list: A list of tuples where each tuple is (start_index, end_index).
    """
    result = []
    prefix_sum = 0
    hashmap = {}

    for i, num in enumerate(arr):
        prefix_sum += num

        # Case 1: If prefix_sum is zero, subarray starts from index 0
        if prefix_sum == 0:
            result.append((0, i))

        # Case 2: If prefix_sum seen before, subarrays exist
        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start + 1, i))

        # Store the prefix_sum occurrence
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = []
        hashmap[prefix_sum].append(i)

    return result


# Example usage
if __name__ == "__main__":
    arr = [1, 2, -3, 3, -1, 2]
    print("Input Array:", arr)
    print("Subarrays with Zero Sum:", find_subarrays_with_zero_sum(arr))
