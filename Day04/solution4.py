"""
Day04 Solution: Merge Two Sorted Arrays (In-place) using Gap Method
"""

from typing import List, Tuple

def next_gap(gap: int) -> int:
    """Calculate next gap size."""
    if gap <= 1:
        return 0
    return (gap + 1) // 2

def merge_in_place(arr1: List[int], arr2: List[int]) -> Tuple[List[int], List[int]]:
    """Merge two sorted arrays in-place without using extra space."""
    m, n = len(arr1), len(arr2)
    total = m + n
    gap = next_gap(total)

    while gap > 0:
        i = 0
        while i + gap < total:
            j = i + gap

            # figure out whether i/j are in arr1 or arr2
            if i < m:
                ai_list, ai_idx = arr1, i
            else:
                ai_list, ai_idx = arr2, i - m

            if j < m:
                aj_list, aj_idx = arr1, j
            else:
                aj_list, aj_idx = arr2, j - m

            if ai_list[ai_idx] > aj_list[aj_idx]:
                ai_list[ai_idx], aj_list[aj_idx] = aj_list[aj_idx], ai_list[ai_idx]

            i += 1

        gap = next_gap(gap)

    return arr1, arr2

# -------- Run Example --------
if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    print("Before merge:")
    print("arr1 =", arr1)
    print("arr2 =", arr2)

    merge_in_place(arr1, arr2)

    print("\nAfter merge:")
    print("arr1 =", arr1)
    print("arr2 =", arr2)
