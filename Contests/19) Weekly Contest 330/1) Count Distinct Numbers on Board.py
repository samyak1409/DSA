"""
https://leetcode.com/problems/count-distinct-numbers-on-board
"""


def distinct_integers(n: int) -> int:
    """"""

    # For n > 2, n % (n-1) == 1 thus n-1 will be added on the board the next day.
    # As the operations are performed for so long time, all the numbers lesser than n except 1 will be added to the
    # board.
    # What will happen if n == 1?

    # 1) Optimal (Realize): TC = O(1); SC = O(1)
    # "Intuition:
    # "for 10^9 days", it's quite a long duration. And n is much smaller than the number of days.
    # It's a brain-teaser, the duration is long enough to generate all cards.
    # Prove:
    # Assume n is on the board, n % (n-1) == 1 if n > 2, so n-1 will be on the board, then n-2 will be on the board,
    # same for n-3,n-4 .... 3, 2. So for any n > 1, 2,3,4...n will be on the board finally, we return n-1.
    # For n = 1 at first, nothing happens, we return 1.
    # So we can return n > 1 ? n - 1 : 1;"
    # -https://leetcode.com/problems/count-distinct-numbers-on-board/solutions/3111651/java-c-python-return-n-1

    """
    return n-1 if n != 1 else n
    """
    # Shortened:
    return n-1 or n
