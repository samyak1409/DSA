"""
https://leetcode.com/problems/equal-sum-grid-partition-ii
"""


def can_partition_grid(grid: list[list[int]]) -> bool:
    """"""

    # Almost did this in the contest, would've got rank ~1k, and AIR ~100.

    # This solution is implemented on top of the first implementation in `3546. Equal Sum Grid Partition I`.

    # 1) Optimal (Compare the sum while iterating; HashMap to track occurrences): TC = O(m*n); SC = O(m*n)
    # > Not hard
    # Main part of solving this is handling the edge cases to avoid disconnecting the individual sections.
    # Check the code comments.

    from itertools import chain

    # Helper:
    def func(grid_: list[list[int]], remaining: int, hm1_: dict[int, int]) -> bool:
        curr_sum = 0
        hm2 = {}
        row_cnt, col_cnt = len(grid_), len(grid_[0])
        # Trying every horizontal cut iteratively:
        for i, row in enumerate(grid_):
            # Update sums and hashmaps to remove this row from lower section and add to upper section:
            row_sum = sum(row)
            remaining, curr_sum = remaining-row_sum, curr_sum+row_sum
            for num in row:
                hm1_[num] -= num
                hm2[num] = hm2.get(num, 0) + 1
            # If at any point, curr_sum == remaining, means we can cut in equal halves:
            if curr_sum == remaining:
                return True
            # If lower section's sum is greater:
            if remaining > curr_sum:
                # `diff` is the element that we can discount in lower section to make the sums equal:
                diff = remaining - curr_sum
                # Now, handling two edge cases to avoid disconnecting the individual sections:
                # Edge case 1:
                # If only one column is there: e.g. `[[6], [2], [3], [4]]`
                # Then we can't discount `3` to make the sums of `[[6]]` & `[[2], [3], [4]]` equal, since it'd
                # disconnect the lower section.
                # So, if col cnt is 1:
                if col_cnt == 1:
                    # Then, we can only discount the TOP or BOTTOM element in the lower section:
                    if diff in [grid_[i+1][0], grid_[-1][0]]:
                        return True
                else:
                    # Edge case 2:
                    # (If only one row is there? No, we don't need to handle this, since we're making a horizontal cut,
                    # we would never find a single element to discount, and hence no chance of disconnection.)
                    # Element to discount could not be in the middle elements of the section with only single row, e.g.
                    # `[[1, 2, 4], [2, 3, 5]]`
                    # We can't discount `3` to make the sections `[[1, 2, 4]]` & `[[2, 3, 5]]` equal.
                    # So, if the next row is the last row:
                    if i+1 == row_cnt-1:
                        # Then, we can only discount the elements on the two ends:
                        if diff in [grid_[i+1][0], grid_[i+1][-1]]:
                            return True
                    # After separately handling the edge cases, we can discount any element:
                    else:
                        if hm1_.get(diff):
                            return True
            # Else if upper section's sum is greater:
            elif curr_sum > remaining:
                # `diff` is the element that we can discount in upper section to make the sums equal:
                diff = curr_sum - remaining
                # Edge case handling similar to above:
                # Edge case1:
                if col_cnt == 1:
                    if diff in [grid_[0][0], grid_[i][0]]:
                        return True
                else:
                    # Edge case 2:
                    if i == 0:
                        if diff in [grid_[0][0], grid_[0][-1]]:
                            return True
                    else:
                        # After separately handling the edge cases, we can discount any element:
                        if hm2.get(diff):
                            return True
        return False

    # Total sum of the grid:
    remaining_sum = sum(chain(*grid))
    # Save the freq in hashmap (using `Counter` gives TLE, so `dict`):
    hm1 = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            hm1[grid[i][j]] = hm1.get(grid[i][j], 0) + 1

    # Row wise or column wise:
    # `zip(*grid)`: neat trick to transpose a 2d arr
    return func(grid, remaining_sum, hm1) or func([list(row) for row in zip(*grid)], remaining_sum, hm1)
