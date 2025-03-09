"""
https://leetcode.com/problems/fruits-into-baskets-ii
"""


def num_of_unplaced_fruits(fruits: list[int], baskets: list[int]) -> int:
    """"""

    # 1) Brute-force (Simulate: Nested Loop): TC = O(n^2); SC = O(n)

    placed = 0
    for f in fruits:
        for i, b in enumerate(baskets):
            # If basket not already used, and can store current fruit:
            if b and b >= f:
                placed += 1
                baskets[i] = 0  # mark / flag
                break
    return len(fruits) - placed
