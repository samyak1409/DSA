"""
https://leetcode.com/problems/unique-3-digit-even-numbers
"""


def total_numbers(digits: list[int]) -> int:
    """"""

    # 1) Sub-optimal (Using `itertools.permutations`): TC = SC = O(nP3) ~= O(n^3)

    """
    from itertools import permutations

    hs = set()  # track uniques
    for p in permutations(digits, r=3):  # O(nP3) {max = 10P3 = 720}
        if p[-1] % 2 == 0 and p[0]:  # if even and no leading zero
            hs.add(p)  # O(3)
    return len(hs)
    """

    # 2) Optimal (Iterate on all even 3-digit nums: 100 to 999): TC = O(n^3-n^2) ~= O(n^3); SC = O(n)

    from collections import Counter

    freq = Counter(digits)  # to efficiently check presence of `num`; TC = SC = O(n)
    ans = 0
    for num in range(100, 1000, 2):  # O((n^3-n^2)/2) {450}
        ans += Counter(map(int, str(num))) <= freq  # O(3)
    return ans
