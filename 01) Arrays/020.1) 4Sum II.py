"""
https://leetcode.com/problems/4sum-ii
"""


def four_sum_count(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    """"""

    # https://leetcode.com/problems/4sum-ii/discuss/1740606/Going-from-O(N4)-greater-O(N3)-greater-O(N2)-JavaC++

    # 0) [TLE] Brute-force (4 Loops: Check every possible pair.): TC = O(n^4); SC = O(1)

    """
    # Hash (0); Search (4):
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            for num3 in nums3:
                for num4 in nums4:
                    if num1+num2+num3+num4 == 0:
                        count += 1
    return count
    """

    # 1) [TLE] Better (Using HashMap): TC = O(n^3); SC = O(n)
    # num1+num2+num3+num4 = 0 => num1+num2+num3 = -num4

    """
    # Hash (1):
    from collections import Counter
    freq = Counter(nums4)
    # Search (3):
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            for num3 in nums3:
                count += freq[-num1-num2-num3]
    return count
    """

    # 2) Optimal (Using HashMap Consciously 😐): TC = O(n^2); SC = O(n^2)
    # num1+num2+num3+num4 = 4 => num1+num2 = -num3-num4

    # Stefan Pochmann Supremacy https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python:
    """
    from collections import Counter
    freq = Counter(num3+num4 for num4 in nums4 for num3 in nums3)
    return sum(freq[-num1-num2] for num2 in nums2 for num1 in nums1)
    """

    # Hash (2):
    from collections import Counter
    freq = Counter()
    for num3 in nums3:
        for num4 in nums4:
            freq[num3+num4] += 1
    # Search (2):
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            count += freq[-num1-num2]
    return count
