# Day 3 - 30 Days Programming Challenge  
📅 Date: 17th August 2025  

## Problem: Find the Duplicate Number  

### Problem Statement  
You are given an array `arr` containing **n+1 integers**, where each integer is in the range `[1, n]` inclusive.  
There is exactly one duplicate number in the array, but it may appear more than once.  

Your task is to **find the duplicate number without modifying the array and using constant extra space**.  

---

### Example  
**Input:**  
`arr = [2, 5, 1, 4, 3, 2]`  

**Output:**  
`Duplicate number: 2`  

---

### Solution Approach  
We use **Floyd’s Tortoise and Hare Algorithm (Cycle Detection)**:  
1. Treat the array as a linked list where each index points to the next element.  
2. Use two pointers (`slow`, `fast`) to detect a cycle.  
3. Once they meet, reset one pointer to start and move both one step at a time until they meet again.  
4. The meeting point is the duplicate number.  

---

### Python Solution
```python
def findDuplicate(arr):
    slow = arr[0]
    fast = arr[0]

    # Detect cycle
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Find duplicate
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow
