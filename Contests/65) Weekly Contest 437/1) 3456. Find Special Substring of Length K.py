"""
https://leetcode.com/problems/find-special-substring-of-length-k
"""


def has_special_substring(s: str, k: int) -> bool:
    """"""

    # 1) Brute-force (Check every k-len substr): TC = O((n-k)*k); SC = O(k) {which can be avoided as well}

    """
    # One by one start from every index:
    for i in range((n:=len(s))-k+1):
        # Check if the substr is made up of only one char, and if the neighbouring elements (if exist) are different:
        if len(set(s[i:i+k])) == 1 and (i == 0 or s[i-1] != s[i]) and (i+k == n or s[i+k] != s[i+k-1]):
            # Return if we've found the substr with all the three conditions satisfied:
            return True
    return False
    """

    # 2) Optimal (Sliding Window): TC = O(n); SC = O(1)
    # Similar to https://leetcode.com/problems/max-consecutive-ones.

    curr, cnt = None, 0
    for char in s:
        # If char same, ++`cnt`:
        if char == curr:
            cnt += 1
        # Else, change `curr`:
        else:
            # When the element CHANGES, first check if the count was what we want:
            if cnt == k:
                return True
            curr = char
            cnt = 1
    # Also, to check for the last char (when there's no next element so above check case never hits):
    return cnt == k
