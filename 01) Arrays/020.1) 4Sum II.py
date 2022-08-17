"""
https://leetcode.com/problems/4sum-ii
"""


def four_sum_count(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (4 Loops): TC = O(n^4); SC = O(1)

    # 1.1) [WA, TLE] Better (Sort & Two Pointers): TC = O(n^3); SC = O(1)
    # WA: Same reason as "019.4) Count Good Meals.py"'s "1)".

    """
    n = len(nums1)
    num3, nums4 = sorted(nums3), sorted(nums4)  # new local vars
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            req_sum = -num1-num2
            i, j = 0, n-1
            while i < n and j >= 0:
                sum_ = nums3[i] + nums4[j]
                if sum_ < req_sum:
                    i += 1
                elif sum_ > req_sum:
                    j -= 1
                else:  # (if sum_ == req_sum)
                    count += 1
                    i, j = i+1, j-1
    return count
    """

    # 1.2) [TLE] Better (Using HashMap): TC = O(n^3); SC = O(1)

    """
    from collections import Counter
    hashmap = Counter(nums4)
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            for num3 in nums3:
                count += hashmap[-num1-num2-num3]
    return count
    """

    # 2) Optimal (Using HashMap Consciously 😐): TC = O(n^2); SC = O(n^2)
    # https://leetcode.com/problems/4sum-ii/discuss/1740606/Going-from-O(N4)-greater-O(N3)-greater-O(N2)-JavaC%2B%2B
    # https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
    # https://leetcode.com/problems/4sum-ii/discuss/175783/Hash-Java-with-Explanations
    # We aim to find all possible A[i] + B[j] + C[k] + D[l] = 0, that is,
    # A[i] + B[j] = -(C[k] + D[l])
    # In other words, we need to count the number of all possible two-sums between A and B that equals to opposite of
    # any two-sum between C and D.
    # Thus, we enumerate all two-sums between C and D, and store sum-to-frequency mappings for reference.

    # Stefan Pochmann Supremacy:
    """
    from collections import Counter
    frequency = Counter(num1+num2 for num1 in nums1 for num2 in nums2)
    return sum(frequency[-num3-num4] for num3 in nums3 for num4 in nums4)
    """

    from collections import Counter
    frequency = Counter()
    for num1 in nums1:
        for num2 in nums2:
            frequency[num1+num2] += 1
    count = 0
    for num3 in nums3:
        for num4 in nums4:
            count += frequency[-num3-num4]
    return count
