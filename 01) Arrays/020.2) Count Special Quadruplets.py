"""
https://leetcode.com/problems/count-special-quadruplets
"""


def count_quadruplets(nums: list[int]) -> int:
    """"""

    # 0) Brute-force (4 Loops): TC = O(n^4); SC = O(1)
    # N is very small, how can we use that? Can we check every possible quadruplet?

    """
    n = len(nums)
    count = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1
    return count
    """

    # The order is important here, therefore we cannot use the two pointers approach (which requires sorting).
    # 1) Better (HashMap): TC = O(n^3); SC = O(n)
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1452628/O(n4)-200-ms-vs.-O(n3)-16-ms
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1456709/Python-99-Clean-Code-Walkthrough-From-O(4)-greater-O(3)-greater-O(2)

    from collections import Counter

    n = len(nums)
    count = 0
    for d in range(n-1, -1, -1):
        for c in range(d-1, -1, -1):
            req_sum = nums[d] - nums[c]  # since A+B+C = D => D-C = B+A
            hashmap = Counter()
            for b in range(c-1, -1, -1):
                num2 = nums[b]
                count += hashmap[req_sum-num2]  # `req_sum-num2` = num1
                hashmap[num2] += 1
    return count

    # 2) Optimal (HashMap): TC = O(n^2); SC = O(n^2)
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1446988/JavaC++Python3-Real-O(n2)-solution
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1456709/Python-99-Clean-Code-Walkthrough-From-O(4)-greater-O(3)-greater-O(2)
    # https://leetcode.com/problems/count-special-quadruplets/discuss/1451080/JavaPython-O(n2)-solution-with-explanation
    # Similar to `020.1) 4Sum II.py`'s `2)`.
