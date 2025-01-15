"""
https://leetcode.com/problems/zigzag-grid-traversal-with-skip
"""


def zigzag_traversal(grid: list[list[int]]) -> list[int]:
    """"""

    # 1) Optimal (Simulate using nested for loop): TC = O(m*n); SC = O(1)

    col = len(grid[0])
    ans = []
    for i in range(len(grid)):
        start, stop, step = (0, col, 2) if i % 2 == 0 else (-1 if col % 2 == 0 else -2, -col-1, -2)
        for j in range(start, stop, step):
            ans.append(grid[i][j])
    return ans
