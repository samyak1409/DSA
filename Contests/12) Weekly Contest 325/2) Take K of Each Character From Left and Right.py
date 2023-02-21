"""
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
"""


def take_characters(s: str, k: int) -> int:
    """"""

    # 1) Optimal (Two Pointers): TC = O(n); SC = O(1)
    # Start by counting the frequency of each character and checking if it is possible.
    # If you take i characters from the left side, what is the minimum number of characters you need to take from the
    # right side? Find this for all values of i in the range 0 ≤ i ≤ s.length.
    # Use a two-pointers approach to avoid computing the same information multiple times.
    # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2947980/c-two-pointer-solution-o-n

    from collections import Counter

    if k == 0:  # edge case
        return 0

    n = len(s)
    count = Counter({'a': 0, 'b': 0, 'c': 0})  # `Counter` for easy working with counts;
    # imp to init with `{'a': 0, 'b': 0, 'c': 0}` so that count.values() == dict_values([0, 0, 0]) (which represents the
    # counts of a, b, and c)

    # Putting `j` to its init position:
    for j in range(n-1, -1, -1):
        count[s[j]] += 1
        if all(map(lambda c: c >= k, count.values())):  # done: "at least k of each character"
            break
    else:  # "return -1 if it is not possible to take k of each character"
        return -1

    minimum = n-j  # i.e. choosing 0 chars from left & minimum required from right
    for i in range(n):
        count[s[i]] += 1  # count the char which is at i
        while j < n and count[s[j]] > k:  # if count of the char at j > k:
            count[s[j]] -= 1  # un-count it
            j += 1  # and shift j ahead
        minimum = min(minimum, i+1 + n-j)  # update ans. if require; `i+1` & `n-j`: chars from left & right respectively
    return minimum

    # Worth mentioning that this question can be transformed and then be solved by Sliding Window!! See the awesome
    # observation here:
    # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2948183/python-clean-12-line-sliding-window-solution-with-explanation
    # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2947988/sliding-window-maximum-o-n-c-java-python3
