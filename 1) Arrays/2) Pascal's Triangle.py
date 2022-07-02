"""
https://leetcode.com/problems/pascals-triangle
"""


from typing import List


def generate(num_rows: int) -> List[List[int]]:

    # 1) Aam Zindagi: TC = O(n^2); SC = O(1)

    """
    ans = [[1]]  # initialization

    # Summation using a nested for loop:
    for i in range(num_rows-1):  # n-1 iterations ✔
        ans.append([1])  # prefix 1
        for j in range(i):  # iteration range: [0, n-2] ✔
            ans[i+1].append(ans[i][j]+ans[i][j+1])  # middle numbers
        ans[i+1].append(1)  # suffix 1

    return ans
    """

    # 2) Mentos Zindagi https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map: TC = O(n^2); SC = O(1)

    """
    Explanation: Any row can be constructed using the offset sum of the previous row.
    
    Example:
              1 3 3 1  
            +   1 3 3 1
            = 1 4 6 4 1
    """

    ans = [[1]]
    for _ in range(num_rows-1):
        ans.append([x+y for x, y in zip([0]+ans[-1], ans[-1]+[0])])  # using list comprehension
        # ans.append(list(map(lambda x, y: x+y, [0]+ans[-1], ans[-1]+[0])))  # using lambda function
    return ans
