"""
https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals
"""


def longest_common_prefix(words: list[str]) -> list[int]:
    """"""

    # 1) Optimal: TC = O(n); SC = O(n)
    # (TC = SC = O(n) since "The sum of words[i].length is smaller than or equal 10^5.")

    # 1.1) LCP, HashMap, HashSet, Sorting:
    # [Came up with in the contest. Easy.]
    # Intuition:
    # First of all, this is obvious that we need to pre-compute and save the LCPs of all the adjacent couples.
    # Now, since we want the largest LCP values, we can maintain a mapping of LCP lengths to hashset of tuples of
    # indices of the couple pair which lead to this particular LCP length. And then we can sort the mapping by the keys
    # i.e. LCP lengths in order to get the largest values first, after this, we just need to discount the pairs one by
    # one, and if the hashset becomes empty, means we need to move to the next LCP length.

    from collections import defaultdict

    # Helper function to calc. LCP length:
    def lcp(i1: int, i2: int) -> int:
        cnt = 0
        for c1, c2 in zip(words[i1], words[i2]):
            if c1 == c2:
                cnt += 1
            else:
                break
        return cnt

    hm = defaultdict(set)
    # Build mapping:
    for i in range((n:=len(words))-1):  # TC = SC = O(n)
        hm[lcp(i, i+1)].add((i, i+1))
    # print(hm)  # debug

    sorted_lcp_cnts = sorted(hm.keys(), reverse=True)  # TC = O(sqrt(n)*log2(sqrt(n)))
    # Why? Similar logic as there in previous Q. Since keys are unique, max unique LCP lengths ~sqrt(n), because
    # "The sum of words[i].length is smaller than or equal 10^5.", so we would only be able to go from 1 to ~sqrt(n),
    # and that would cap `10^5` total length. (Sum of n terms = sum(1, 2, ..., n) = n(n+1)/2)

    sorted_lcp_cnts.append(0)

    # print(sorted_lcp_cnts)  # debug

    ans = []

    # Loop on words:
    for i in range(n):
        # For every index, discount the two possible couple pairs, and add the largest LCP length to the ans:
        j = 0  # index for `sorted_lcp_cnts`
        pair_cnt = len(hm[sorted_lcp_cnts[j]])  # init the pair count for the first (largest) LCP length
        # Two possible pairs are possible for any index (other than indices on the two ends, no need to handle those
        # cases explicitly since pairs like (-1, 0) wouldn't be found in our pair hashsets, so no effect.):
        for pair in ((i-1, i), (i, i+1)):
            # If pair is there in hashset, meaning index `i` was used for one LCP length in the hashset, hence we need
            # to discount that one:
            if pair in hm[sorted_lcp_cnts[j]]:
                pair_cnt -= 1
                # If at any point pair cnt for current LCP length become 0, means we need to move to the next LCP
                # length:
                if pair_cnt == 0:
                    j += 1
                    pair_cnt = len(hm[sorted_lcp_cnts[j]])
        # If `i` is on the edge of the list:
        if i == 0 or i == len(words)-1:
            ans.append(sorted_lcp_cnts[j])
        # Else, we can have a new LCP length as well, made via `i-1` and `i+1` pairing when `i` is removed:
        else:
            ans.append(max(sorted_lcp_cnts[j], lcp(i-1, i+1)))

    return ans

    # 1.2) LCP, Prefix-Suffix:
    # Standard way to solve this problem, I guess. This is easy as well.
    # https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/solutions
