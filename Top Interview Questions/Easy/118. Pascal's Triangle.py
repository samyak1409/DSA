"""
https://leetcode.com/problems/pascals-triangle/
"""


from typing import List


def generate(num_rows: int) -> List[List[int]]:  # TC = O(n^2) = SC

    # 1) Aam Jeevan:

    """
    ans = [[1], [1, 1]]  # initialization

    if num_rows in (1, 2):  # no summation
        return ans[:num_rows]

    # Summation using a nested for loop:

    for i in range(1, num_rows-1):  # (num_rows-2) times

        ans.append([1])  # (prefix)

        for j in range(i):  # (1 to num_rows-2) times
            ans[i+1].append(ans[i][j]+ans[i][j+1])  # mid. numbers' calc

        ans[i+1].append(1)  # (suffix)

    return ans
    """

    # 2) Mentos Jeevan: https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map

    """
    Explanation: Any row can be constructed using the offset sum of the previous row.
    
    Example:
              1 3 3 1 0 
            + 0 1 3 3 1
            = 1 4 6 4 1
    """

    ans = [[1]]
    for _ in range(num_rows-1):
        ans.append(list(map(lambda x, y: x+y, [0]+ans[-1], ans[-1]+[0])))
    return ans
