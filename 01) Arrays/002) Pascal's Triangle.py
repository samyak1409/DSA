"""
https://leetcode.com/problems/pascals-triangle
"""


from typing import List


def generate(num_rows: int) -> List[List[int]]:

    # 1) Aam Zindagi: TC = O(n^2); SC = O(n) {because on any iteration we only require previous row in order to calc. the present row,
    #                                         and the other rows are just being saved for the purpose of returning the answer}

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

    # 2) Mentos Zindagi https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map: TC = O(n^2); SC = O(n) {because
    # on any iteration we only require previous row in order to calc. the present row, and the other rows are just being saved for the purpose of returning the answer}

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

    # NOTE: Two other variations of this question can also be asked in the interview (https://youtu.be/6FLvhQjZqvM):

    # VARIATION 1) Print the value at mth row and nth column.        1            -> 1
    # Input: m = 5; n = 3                                          1   1          -> 2
    # Output: 6                                                  1   2   1        -> 3
    #                                                          1   3   3   1      -> 4
    # Solution:                                              1   4   6   4   1    -> 5
    #
    # Approach 0) Using the default method (sum of the two numbers directly above it): TC = O(n^2); SC = O(n)
    #
    # Approach 1) Can be easily calculated using combinations formula C(m-1, n-1): TC = O(n) {because combinations contain factorial, which is O(n)}; SC = O(1)
    #
    #             C(m-1, n-1) = (m-1)! / {(n-1)! * [(m-1)-(n-1)]!} = (m-1)! / [(n-1)! * (m-n)!]
    #             Let i = m-1; j = n-1 => Formula = C(i, j) = i! / [j! * (i-j)!]
    #             So, for Input: m = 5; n = 3
    #                            => i = 4; j = 2
    #                            => Output: C(4, 2) = 4! / [2! * (4-2)!]
    #                                               = 4! / (2!*2!)
    #                                               = (4*3*2*1) / (2*1*2*1)
    #                                               = (4*3) / (2*1)
    #                                               = 12 / 2
    #                                               = 6

    # VARIATION 2) Print mth row.            1            -> 1
    # Input: m = 5                         1   1          -> 2
    # Output: [1, 4, 6, 4, 1]            1   2   1        -> 3
    #                                  1   3   3   1      -> 4
    # Solution:                      1   4   6   4   1    -> 5
    #
    # Approach 0) Using the default method (sum of the two numbers directly above it): TC = O(n^2); SC = O(n)
    #
    # Approach 1) Using combinations formula C(m-1, n-1): TC = O(n^2) {nCr for n items of a row}; SC = O(1)
    #
    # Approach 2) Using pattern observed from combinations formula C(m-1, n-1): TC = O(n); SC = O(1)
    #
    #             Let's take a look when we apply combinations formula on an entire row, let's take m = 7, (n = [1, 2, 3, 4, 5, 6, 7])
    #             C(6, 0) = 6! / [0! * (6-0)!]                             = 1   (directly 1 (initialization))
    #             C(6, 1) = 6! / [1! * (6-1)!] =           6 / 1           = 6   (next = previous*6/1 =  1*6/1 = 6)
    #             C(6, 2) = 6! / [2! * (6-2)!] =         6*5 / 2*1         = 15  (next = previous*5/2 =  6*5/2 = 15)
    #             C(6, 3) = 6! / [3! * (6-3)!] =       6*5*4 / 3*2*1       = 20  (next = previous*4/3 = 15*4/3 = 20)
    #             C(6, 4) = 6! / [4! * (6-4)!] =     6*5*4*3 / 4*3*2*1     = 15  (next = previous*3/4 = 20*3/4 = 15)
    #             C(6, 5) = 6! / [5! * (6-5)!] =   6*5*4*3*2 / 5*4*3*2*1   = 6   (next = previous*2/5 = 15*2/5 = 6)
    #             C(6, 6) = 6! / [6! * (6-6)!] = 6*5*4*3*2*1 / 6*5*4*3*2*1 = 1   (next = previous*1/6 =  6*1/6 = 1)
    #
    #             Hence, we got the pattern which can be easily programmed with O(n) time.

    # INTERESTINGLY: Using this approach for the main question (building full Pascal Triangle), will reduce its SC from O(n) to O(1)!
