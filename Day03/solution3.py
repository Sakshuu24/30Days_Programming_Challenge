def findDuplicate(arr):
    # Floyd’s Tortoise and Hare Algorithm (Cycle Detection)
    slow = arr[0]
    fast = arr[0]

    # First phase: Find intersection point
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Second phase: Find entrance to the cycle (duplicate number)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


# Example usage
if __name__ == "__main__":
    arr = [2, 5, 1, 4, 3, 2]
    print("Duplicate number:", findDuplicate(arr))
