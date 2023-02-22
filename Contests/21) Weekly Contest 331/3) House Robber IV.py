"""
https://leetcode.com/problems/house-robber-iv
"""


def min_capability(nums: list[int], k: int) -> int:
    """"""

    # -1) [WA] Optimal (Greedy): TC = O(n*log(n)); SC = O(n)
    # Approach: Start with the min money, and choose next allowed min money.
    # Dry run with ([9,6,20,21,8], 3) to find out why WA.

    """
    indices = set()  # will store the positions of the houses which are robbed
    # Loop on money in increasing (non-decreasing to be accurate) order:
    for i, money in sorted(enumerate(nums), key=lambda tup: tup[1]):
        if i-1 not in indices and i+1 not in indices:  # if adjacent houses of this house are not robbed
            indices.add(i)  # rob this house
            if not (k := k-1):  # decrement k, and as soon as k becomes 0, i.e. we rob k houses, 
                # return ans, which will be the max of all the houses robbed, which will be the latest house only
                return money
    """

    # Can we use binary search to find the minimum value of a non-contiguous subsequence of a given size k?

    # 1) Optimal (Binary Search): TC = O(log2(10^9) * n); SC = O(1)
    # Initialize the search range with the minimum and maximum elements of the input array.
    # Use a check function to determine if it is possible to select k non-consecutive elements that are less than or
    # equal to the current "guess" value.
    # Adjust the search range based on the outcome of the check function, until the range converges and the minimum
    # value is found.
    # https://leetcode.com/problems/house-robber-iv/solutions/3143697/java-c-python-binary-search-o-1-space

    # Helper Function:
    def check(val: int) -> bool:
        # Check if with this particular val, choosing k non-adjacent houses is possible or not:
        # Read why greedy is working here: https://leetcode.com/problems/house-robber-iv/solutions/3143685/binary-search
        count = 0
        last = -2  # index of last chosen house
        for i, money in enumerate(nums):  # O(n)
            if money <= val and i-1 != last:
                count += 1  # consider this house
                last = i  # update
                if count == k:  # if we got enough houses, stop
                    break
        return count == k

    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure_for_finding_the_leftmost_element:
    lo, hi = min(nums), max(nums)+1
    while lo < hi:  # O(log2(10^9)) = O(30) = O(1)
        guess = (lo + hi) // 2
        if check(guess):  # current guess val is valid, let's see if we can get a smaller valid val
            hi = guess
        else:  # count < k, guess was invalid, we need a larger val
            lo = guess + 1
    return lo  # or hi

    # "most of the time ( >99% ), in minimax problems we use Binary search.
    # Identification: maximize the minimum or minimize the maximum certain function."
    # -https://leetcode.com/discuss/general-discussion/3143635/Weekly-Contest-331/1788635
    # "one important tip for you. Whenever a problem involves finding maximum or minimum just think about using binary
    # search to solve it. This tip will definitely help you. I failed to solve one straight forward binary search
    # problem in ICPC regionals and since then I started using the above tip and never failed to solve a binary search
    # problem."
    # -https://leetcode.com/discuss/general-discussion/3143635/Weekly-Contest-331/1788749

    # "
    # When we min-max one capacity to do something,
    # we can use binary search.
    #
    # When use binary search,
    # I suggest you using my template:
    #
    # while lo < hi:
    #     mid = (lo + hi) // 2
    #     if check():
    #         hi = mid
    #     else:
    #         lo = mid + 1
    # return lo
    # "
    # -https://leetcode.com/problems/house-robber-iv/solutions/3143697/java-c-python-binary-search-o-1-space
