"""
https://leetcode.com/problems/equal-sum-grid-partition-i
"""


from typing import Iterator


def can_partition_grid(grid: list[list[int]]) -> bool:
    """"""

    # 1) Optimal (Calc. total sum, compare while iterating): TC = O(m*n); SC = O(1)

    """
    from itertools import chain

    # Helper:
    def func(grid_: list[list[int]] | Iterator[tuple[int]], remaining: int) -> bool:
        curr_sum = 0
        # Trying every horizontal cut iteratively:
        for row in grid_:
            # Update sums to remove this row from lower section and add to upper section:
            row_sum = sum(row)
            remaining, curr_sum = remaining-row_sum, curr_sum+row_sum
            # If at any point, curr_sum == remaining, means we can cut in equal halves:
            if curr_sum == remaining:
                return True
        return False

    # Total sum of the grid:
    remaining_sum = sum(chain(*grid))

    # Row wise or column wise:
    return func(grid, remaining_sum) or func(zip(*grid), remaining_sum)  # `zip(*grid)`: neat trick to transpose a 2d arr
    """

    # We can also do it using `2 * curr_sum == total_sum` instead of `curr_sum == remaining`:

    """
    from itertools import chain

    # Helper:
    def func(grid_: list[list[int]] | Iterator[tuple[int]]) -> bool:
        curr_sum = 0
        # Trying every horizontal cut iteratively:
        for row in grid_:
            # Update sums to remove this row from lower section and add to upper section:
            curr_sum += sum(row)
            # If at any point, 2 * curr_sum == total_sum, means we can cut in equal halves:
            if 2 * curr_sum == total_sum:
                return True
        return False

    # Total sum of the grid:
    total_sum = sum(chain(*grid))

    # Row wise or column wise:
    return func(grid) or func(zip(*grid))  # `zip(*grid)`: neat trick to transpose a 2d arr
    """

    # With 2 quick optimizations:

    from itertools import chain

    # Helper:
    def func(grid_: list[list[int]] | Iterator[tuple[int]]) -> bool:
        curr_sum = 0
        # Trying every horizontal cut iteratively:
        for row in grid_:
            # Update sums to remove this row from lower section and add to upper section:
            curr_sum += sum(row)
            # If at any point, curr_sum == half_sum, means we can cut in equal halves:
            if curr_sum == half_sum:
                return True
            # Optimization 2:
            if curr_sum > half_sum:
                return False
        return False

    # "Killing two birds with one stone": Calculate half-sum as well as check if the total sum is odd using `divmod`:
    half_sum, total_sum_odd = divmod(sum(chain(*grid)), 2)
    # Optimization 1:
    if total_sum_odd:
        return False

    # Row wise or column wise:
    return func(grid) or func(zip(*grid))  # `zip(*grid)`: neat trick to transpose a 2d arr
