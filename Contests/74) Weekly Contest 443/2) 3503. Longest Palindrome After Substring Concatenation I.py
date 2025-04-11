"""
https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i
"""


def longest_palindrome(s: str, t: str) -> int:
    """"""

    # Wasted time optimizing, but O(n^5) brute-force got AC.
    # That's 2.43e7, not generally AC.
    # - https://leetcode.com/discuss/post/6594489/weekly-contest-443-by-leetcode-88qo/comments/2922700

    # 1) Brute-force (Try every combination of both): TC = O(n^5); SC = O(n)

    # Helper Function:
    def palin(x: str) -> bool:
        # O(n) time but two pass, O(n) space:
        # return x == x[::-1]
        # O(n) time and one pass, O(1) space:
        for i in range(len_//2):
            if x[i] != x[~i]:  # `~i` = `-i-1`
                return False
        return True

    ans = 0
    # Try all the substr of `s`:
    for i1 in range(len(s)+1):
        for j1 in range(i1, len(s)+1):
            lt = s[i1:j1+1]
            # With all the substr of `t`:
            for i2 in range(len(t)+1):
                for j2 in range(i2, len(t)+1):
                    rt = t[i2:j2+1]
                    # And check if palin:
                    # (Checking `len_ > ans` before `palin()`: optimization.)
                    if (len_:=len(lt)+len(rt)) > ans and palin(x=lt+rt):
                        ans = len_
    # One edge case:
    # Since we can choose one of the substr as empty, we also need to consider the concatenations:
    # `substr(s) + ''` and `'' + substr(t)`
    # Handled this by using `+1` in `range()`. (This helps in making a 0-len substr.)

    return ans

    # 2) Optimal (): TC = O(n^3); SC = O(n)
    # https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/solutions/6594619/easiest-python-solution-beats-95-solutions-beginner-friendly
