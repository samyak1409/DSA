"""
https://leetcode.com/problems/extra-characters-in-a-string
"""


def min_extra_char(s: str, dictionary: list[str]) -> int:
    """"""

    # Can we use Dynamic Programming here?
    # Define DP[i] as the min extra character if breaking up s[0:i] optimally.

    # 1) [TLE] Brute-force (Recursion): TC = O(2^n * n); SC = O(n^2)

    """
    # Recursive Function:
    def get_extra(start: int = 0) -> int:

        # Base case:
        if start == s_len:
            return 0  # recurse out

        return min((0 if s[start:end+1] in word_set else end-start+1) + get_extra(start=end+1) for end in range(start, s_len))
        # `s[start:end+1]`: curr sub-str
        # `(0 if s[start:end+1] in word_set else end-start+1)`: no. of extra chars for curr sub-str
        # `get_extra(start=end+1)`: returns extra for remaining part of the sub-str using recursion

    s_len = len(s)
    word_set = set(dictionary)  # for O(1) lookup; TC = O(n^2); SC = O(n^2)
    # Try all partitions using Recursion and return the min:
    return get_extra()  # TC = O(2^n * n); SC = O(n)
    """

    # Turns out it's very similar to the question in the last contest only!!
    # -> Contests/43) Weekly Contest 346/3) 2698. Find the Punishment Number of an Integer.py

    # 1.1) Optimal (Recursion + Memoization): TC = O(n^2); SC = O(n^2)
    # Just apply memoization to the above solution.

    from functools import cache

    # Recursive Function:
    @cache
    def get_extra(start: int = 0) -> int:

        # Base case:
        if start == s_len:
            return 0  # recurse out

        return min((0 if s[start:end+1] in word_set else end-start+1) + get_extra(start=end+1) for end in range(start, s_len))
        # `s[start:end+1]`: curr sub-str
        # `(0 if s[start:end+1] in word_set else end-start+1)`: no. of extra chars for curr sub-str
        # `get_extra(start=end+1)`: returns extra for remaining part of the sub-str using recursion

    s_len = len(s)
    word_set = set(dictionary)  # for O(1) lookup; TC = O(n^2); SC = O(n^2)
    # Try all partitions using Recursion and return the min:
    return get_extra()  # TC = O(n * n); SC = O(n)

    # How it works:
    # leetscode, dictionary = ["leet","code","leetcode"]
    # [l + eetscode]
    # #Make a cut “l” and fix the string
    # #Then get the extra character count for “eetscode” (recursion)
    # #Now “l” is not in dictionary so
    # totalExtra = sizeof(“l”) + nextExtra(got via recursion)
    # //====================================================
    # [le + etscode]
    # #Make a cut “le” and fix the string
    # #Then get the extra character count for “etscode” (recursion)
    # #Noe “le” is not in dictionary
    # totalExtra = sizeof(“le”) + nextExtra(got via recursion)
    # //====================================================
    # [lee + tscode]
    # #Similarly for “lee”
    # //================================================================
    # [leet + scode]
    # #Make a cut “leet” and fix the string
    # #Then get the extra character count for “scode” (recursion)
    # #Now “leet” is in dictionary :) [A relief]
    # totalExtra = 0 + nextExtra(got via recursion)
    # //==================================================================
    # #Similarly other calls are made
    # -https://leetcode.com/problems/extra-characters-in-a-string/solutions/3568666/recursion-top-down-bottom-up-explained-easy-to-understand

    # TC & SC:
    # Note: n is denoting `s.length`, `dictionary.length`, and `dictionary[i].length`
    # How the TC for recursion was 2^n?: Explained in "3) 2698. Find the Punishment Number of an Integer.py" (at bottom)
