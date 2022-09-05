"""
https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid
"""


def min_cost(start_pos: list[int], home_pos: list[int], row_costs: list[int], col_costs: list[int]) -> int:
    """"""

    # 0) Brute-force (Find All Possible Paths): TC = O(m*n); SC = O(m*n)
    # Using Recursion + Memoization, same as what we did in:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/017.2%29%20Minimum%20Path%20Sum.py

    # 1) Optimal (Count Costs for each Row & Column from Start to Home): TC = O(m+n); SC = O(1)
    # Irrespective of what path the robot takes, it will have to traverse all the rows between startRow and homeRow and
    # all the columns between startCol and homeCol.
    # Hence, making any other move other than traversing the required rows and columns will potentially incur more cost
    # which can be avoided.
    # https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/discuss/1598941/JavaC++Python-All-shortest-paths-have-the-same-cost
    # https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/discuss/1598900/C++Python-Simple-Solution-w-Explanation-or-Count-costs-for-each-row-and-column-from-end-to-start

    """
    total_cost = 0
    (start_row, start_col), (end_row, end_col) = start_pos, home_pos
    for r in range(end_row, start_row, 1 if end_row < start_row else -1):
        total_cost += row_costs[r]
    for c in range(end_col, start_col, 1 if end_col < start_col else -1):
        total_cost += col_costs[c]
    return total_cost
    """
    # In short:
    (start_row, start_col), (end_row, end_col) = start_pos, home_pos
    return \
        sum(row_costs[start_row+1:end_row+1] if (start_row < end_row) else row_costs[end_row:start_row]) + \
        sum(col_costs[start_col+1:end_col+1] if (start_col < end_col) else col_costs[end_col:start_col])
