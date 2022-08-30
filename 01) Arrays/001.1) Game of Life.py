"""
https://leetcode.com/problems/game-of-life
"""


def game_of_life(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    # 0) Brute-force (Copy Grid): TC = O(m*n); SC = O(m*n)

    # Follow up: Could you solve it in-place? Remember that the board needs to be updated simultaneously:
    # You cannot update some cells first and then use their updated values to update other cells.
    # 1) Optimal (Using 2 bits to store 2 states): TC = O(m*n); SC = O(1)
    # Easy: https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
    # https://leetcode.com/problems/game-of-life/discuss/73230/C%2B%2B-O(1)-space-O(mn)-time

    # Follow up: In this question, we represent the board using a 2D array. In principle, the board is infinite,
    # which would cause problems when the active area encroaches upon the border of the array
    # (i.e., live cells reach the border). How would you address these problems?
    # https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution
