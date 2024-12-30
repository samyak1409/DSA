"""
https://leetcode.com/problems/find-the-longest-semi-repetitive-substring
"""


def longest_semi_repetitive_substring(s: str) -> int:
    """"""

    # Hint: Since n is small, we can just check every substring, and if the substring is semi-repetitive, maximize the
    # answer with its length.

    # 0) Brute-force (Check every substring): TC = O(n^2); SC = O(1)

    """
    ans = 0
    flag = False  # track if we've seen "adjacent pair of the same digit"
    for i in range(len(s)):  # (`i`: substr start index)
        j = 0  # (just for handling the edge case when len(s) == 1)
        for j in range(i+1, len(s)):  # (`j`: substr end index)
            # If current digit is same as prev digit:
            if s[j] == s[j-1]:
                # If we've already had "adjacent pair of the same digit", we `break`:
                if flag:
                    # We'd only get out of this inner loop because of the two reasons, either we've got to the end of
                    # the str without seeing 2 "adjacent pair of the same digit", or we encountered second "adjacent
                    # pair of the same digit", in the latter case, we need to --j, so that the answer does not consider
                    # the current digit:
                    j -= 1
                    break
                flag = True  # flip the flag
        ans = max(ans, j-i+1)  # (+1 to get the len of substr i to j)
        flag = False  # reset flag
    return ans
    """

    # 0) Optimal (Sliding Window, Greedy): TC = O(n); SC = O(1)

    # Handle the edge case:
    if len(s) == 1:
        return 1

    ans = 0
    flag = False  # track if we've seen "adjacent pair of the same digit"
    i = -1  # (`i`: substr start index)
    next_i = None  # by going greedy, we'd store the index of last seen "adjacent pair of the same digit", as it'd be
    # optimal to start the next window from, when the current window can no more extend
    for j in range(len(s)-1):
        # If current digit is same as prev digit:
        if s[j+1] == s[j]:
            # If we've already had "adjacent pair of the same digit":
            if flag:
                # Current window can no more extend, so update the ans, and set the new starting of our window:
                ans = max(ans, j-i)
                i = next_i
            flag = True  # flip the flag
            next_i = j  # save for future
    # If we don't run into second "adjacent pair of the same digit", and traverse till the end, we'd not have updated
    # the answer with that, so:
    return max(ans, j-i+1)  # noqa

    # (Note that we can also just use the `next_i` var in place of `flag`.)
