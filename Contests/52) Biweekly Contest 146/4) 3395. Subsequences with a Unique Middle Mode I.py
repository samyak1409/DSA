"""
https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i
"""


def subsequences_with_middle_mode(nums: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Try all combinations): TC = O(nC5) {max(n) == 1000, so max(nC5) ~ 1e13}; SC = O(1)

    from itertools import combinations
    from collections import Counter

    ans = 0
    # Try every possible subsequence of len 5:
    for sub_seq in combinations(nums, 5):  # O(nC5) {max(n) == 1000, so max(nC5) ~ 1e13}
        freq = Counter(sub_seq).most_common()  # O(5) = O(1)
        # `freq`: list[tuple[most_common_el, its_count]]
        # print(sub_seq, freq)  # debug
        ans += (freq[0][0] == sub_seq[2]) and (freq[0][1] > freq[1][1] if len(freq) > 1 else True)
        # `freq[0][0] == sub_seq[2]`: if the most common element is middle element
        # `and`
        # `freq[0][1] > freq[1][1] if len(freq) > 1 else True`: there's only one most common element
        ans %= 10**9 + 7
    return ans
