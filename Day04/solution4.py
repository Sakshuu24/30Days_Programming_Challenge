#!/usr/bin/env python3
"""
Day 04 Solution — Merge Two Sorted Arrays (In-place)
"""

from typing import List, Tuple


def next_gap(gap: int) -> int:
    """Calculate next gap (ceil(gap/2)) until it becomes 0."""
    if gap <= 1:
        return 0
    return (gap + 1) // 2


def merge_in_place(arr1: List[int], arr2: List[int]) -> Tuple[List[int], List[int]]:
    """
    Merge arr1 and arr2 in-place using the Gap Method.
    """
    m, n = len(arr1), len(arr2)
    total = m + n
    gap = next_gap(total)

    while gap > 0:
        i = 0
        while i + gap < total:
            j = i + gap

            # Access arr1 or arr2 depending on index
            if i < m:
                ai_list, ai_idx = arr1, i
            else:
                ai_list, ai_idx = arr2, i - m

            if j < m:
                aj_list, aj_idx = arr1, j
            else:
                aj_list, aj_idx = arr2, j - m

            # Swap if out of order
            if ai_list[ai_idx] > aj_list[aj_idx]:
                ai_list[ai_idx], aj_list[aj_idx] = aj_list[aj_idx], ai_list[ai_idx]

            i += 1
        gap = next_gap(gap)

    return arr1, arr2


def main():
    # ✅ Hardcoded input (change here for testing)
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    merge_in_place(arr1, arr2)

    print("Merged arr1:", arr1)
    print("Merged arr2:", arr2)


if __name__ == "__main__":
    main()

