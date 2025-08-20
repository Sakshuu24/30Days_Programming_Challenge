def find_leaders(arr):
    """
    Function to find leaders in an array.
    
    Args:
        arr (list): List of integers.
    
    Returns:
        list: A list of leader elements.
    """
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]  # last element is always a leader
    leaders.append(max_from_right)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Since we traversed from right, reverse to maintain order
    leaders.reverse()
    return leaders


# Example usage
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print("Input Array:", arr)
    print("Leaders:", find_leaders(arr))
