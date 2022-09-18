"""
https://leetcode.com/problems/game-of-life
"""


def game_of_life(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    # 0) Brute-force (Copy Grid): TC = O(m*n); SC = O(m*n)
    # Modifying the input board only, but copying the board, so extra space is being used.
    # So not "in-place", because
    # `In computer science, an in-place algorithm is an algorithm which transforms input using no auxiliary data
    # structure.` - [Wikipedia](https://en.wikipedia.org/wiki/In-place_algorithm)

    """
    from copy import deepcopy

    m, n = len(board), len(board[0])
    original_board = deepcopy(board)  # coz dimensions(board) > 1 (board has nested list); SC = O(m*n)
    # so deepcopy so that it doesn't point to the same nested lists
    for i in range(m):  # TC = O(m*n)
        for j in range(n):  # TC = O(n)
            live_neighbors = sum(original_board[x][y] for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1),
                                                                   (i, j-1),             (i, j+1),    # co-ordinates of
                                                                   (i+1, j-1), (i+1, j), (i+1, j+1))  # neighbors
                                 if 0 <= x < m and 0 <= y < n)  # to prevent index out of bound
            if original_board[i][j]:  # if live cell
                if live_neighbors < 2 or live_neighbors > 3:  # under-population or over-population
                    board[i][j] = 0  # dies
            else:  # if dead cell
                if live_neighbors == 3:  # reproduction
                    board[i][j] = 1  # becomes a live cell
    """
    # Runtime: 33 ms, faster than 95.07% of Python3 online submissions for Game of Life.
    # Memory Usage: 13.9 MB, less than 91.19% of Python3 online submissions for Game of Life.

    # Follow up: Could you solve it in-place? Remember that the board needs to be updated simultaneously:
    # You cannot update some cells first and then use their updated values to update other cells.
    # 1) Optimal (Converting the 1-bit no. to 2-bits, to store old and new state): TC = O(m*n); SC = O(1)
    # Easy: https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
    # https://leetcode.com/problems/game-of-life/discuss/73230/C++-O(1)-space-O(mn)-time
    #
    # Why do we need to track the old state? Obviously because the modifications are needed to be done using the old
    # state only.
    # So, now the question is, which bit should we use for storing old and which bit should we use for storing new
    # state?
    # Let's tryout both the options and see if any of them is beneficial over the other.
    # 1) OldNew (Left Bit for Old State and Right Bit for New State)
    #    -> Preprocess: LEFT-SHIFT all the values by 1 (value <<= 1).
    #    -> Main: Get Old State using 1 RIGHT-SHIFT of value (old_state_val = value >> 1), calculate New State,
    #             and ADD it to the value (value += new_state_val).
    #    -> Finalize: AND all the values with 1 (value &= 1) in order to get the New State.
    # 2) NewOld (Left Bit for New State and Right Bit for Old State)
    #    -> Main: Get Old State using AND of value with 1 (old_state_val = value & 1), calculate New State,
    #             LEFT-SHIFT it by 1 (new_state_val <<= 1), and ADD it to the value (value += new_state_val).
    #    -> Finalize: RIGHT-SHIFT all the values by 1 (value >>= 1) in order to get the New State.
    # So, we can see that the Option 2 doesn't need preprocessing and so it can be done in 2 (instead of 3) passes, so
    # we'll do that.
    # Also, after comparing both the options, 1st one looks useless.

    # Main:
    m, n = len(board), len(board[0])
    for i in range(m):  # TC = O(m*n)
        for j in range(n):  # TC = O(n)
            live_neighbors = sum(board[x][y] & 1 for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1),
                                                              (i, j-1),             (i, j+1),    # co-ordinates of
                                                              (i+1, j-1), (i+1, j), (i+1, j+1))  # neighbors
                                 if 0 <= x < m and 0 <= y < n)  # to prevent index out of bound
            if board[i][j]:  # if live cell
                if live_neighbors in (2, 3):  # (rule 2)
                    # board[i][j] += 1 << 1  # lives on to the next generation
                    # or:
                    board[i][j] = 3  # 01 -> 11
            else:  # if dead cell
                if live_neighbors == 3:  # reproduction
                    # board[i][j] += 1 << 1  # becomes a live cell
                    # or:
                    board[i][j] = 2  # 00 -> 10
    # Finalize:
    for i in range(m):  # TC = O(m*n)
        for j in range(n):  # TC = O(n)
            board[i][j] >>= 1

    # Follow up: In this question, we represent the board using a 2D array. In principle, the board is infinite,
    # which would cause problems when the active area encroaches upon the border of the array
    # (i.e., live cells reach the border). How would you address these problems?
    # https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution
