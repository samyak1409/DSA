"""
https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string
"""


def find_the_longest_balanced_substring(s: str) -> int:
    """"""

    # 0) Brute-force (Check every subarray): TC = O(n^2); SC = O(n)
    # Consider iterating over each subarray and checking if it’s balanced or not.
    # Among all balanced subarrays, the answer is the longest one of them.

    """
    ans = 0

    for i in range(n := len(s)):  # O(n^2)
        z = o = 0
        for j in range(i, n):  # O(n)
            if s[j] == '0':
                z += 1
            else:
                o += 1

            # Check for every subarray:
            if s[i:j+1] == '0'*z + '1'*z:  # TC = SC = O(n)
                ans = max(ans, z*2)

    return ans
    """

    # 0.1) Little Better (in terms of both computational complexities and LOC):
    # https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/solutions/3368279/python-java-c-implemetation

    """
    ss = ''
    while ss in s:
        ss = f'0{ss}1'  # (f-strings with `{}` may be slightly faster and more memory-efficient than using `+`)
    return len(ss)-2
    """

    # 1) Optimal (Smart Counting): TC = O(n); SC = O(1)

    max_streak = zeroes = curr_streak = 0

    for c in s:
        if c == '0':  # if 0 came
            '''
            if curr_streak == 0:  # and no streak is going on
                zeroes += 1
            else:  # if streak is on
                zeroes, curr_streak = 1, 0  # reset
            '''
            # Short:
            if curr_streak != 0:  # and streak is on
                zeroes = curr_streak = 0  # reset
            zeroes += 1
        else:  # if 1 came
            if zeroes:  # if we've 0s
                zeroes -= 1  # one `0` balanced with current `1`
                curr_streak += 1
                max_streak = max(max_streak, curr_streak)  # update ans. if needed

    return max_streak * 2
