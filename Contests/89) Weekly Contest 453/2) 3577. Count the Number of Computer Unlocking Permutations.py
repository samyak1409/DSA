"""
https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations
"""


def count_permutations(complexity: list[int]) -> int:
    """"""

    # Trick problem (https://leetcode.com/discuss/post/6821831/weekly-contest-453-by-leetcode-7ono/comments/3024878)

    # 1) Optimal (Loop, math.factorial): TC = O(n); SC = O(1)
    # Realization that if root i.e. `complexity[0]` < all other elements, means we can decrypt all the computers.
    # Ways = `(n-1)!` since root is fixed, and all others can be shuffled.

    from math import factorial

    # Unlocking all computers is impossible if any of the computer <= root:
    for i in range(1, n:=len(complexity)):
        if complexity[i] <= complexity[0]:
            return 0

    return (factorial(n-1)) % (10**9 + 7)

    # Hasty WA https://leetcode.com/discuss/post/6821831/weekly-contest-453-by-leetcode-7ono/comments/3024880
