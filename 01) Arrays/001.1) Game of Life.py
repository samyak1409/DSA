"""
https://leetcode.com/problems/game-of-life
"""


def game_of_life(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    # 0) Brute-force (Copy Grid): TC = O(m*n); SC = O(m*n)

    # 1) Optimal (Using 2 bits to store 2 states): TC = O(m*n); SC = O(1)
    # Easy: https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
    # https://leetcode.com/problems/game-of-life/discuss/73230/C%2B%2B-O(1)-space-O(mn)-time
    # https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution
