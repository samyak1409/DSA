"""
https://leetcode.com/problems/smallest-palindromic-rearrangement-i
"""


from itertools import chain


def smallest_palindrome(s: str) -> str:
    """"""

    # 1) Optimal: TC = O(n); SC = O(26)
    # [Came up with myself.]
    # Most important observation:
    # At max one char can have odd freq, e.g., "abbba"
    # Proof by trial:
    # Let's try to make a palindromic string with two different chars with odd freq:
    # "abbaba", so as you can see, impossible.
    # So now we can form an algo:
    # Count the freq of all the chars, put half of the chars in sorted order, put one odd char, put the remaining half
    # freq in reverse sorted order.
    # e.g. babab
    # a: 2, b: 3
    # ans = ab + b + ba

    # 1.1) HashMap, Counting Sort: TC = O(n); SC = O(26)

    """
    # Count freq:
    freq = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    for c in s:
        freq[c] += 1

    half = []
    odd = ''
    # Add the 1st half to the arr:
    for c, x in freq.items():
        half.extend(c*(x//2))
        if x % 2:
            odd = c

    # Return 1st half + odd (if there) + 2nd half (reversed):
    # return ''.join(half) + odd + ''.join(half[::-1])
    return ''.join(chain(half, [odd], (half[i] for i in range(len(half)-1, -1, -1))))
    """

    # 1.2) HashMap (Counter), Sort: TC = O(n + 26*log(26)) = O(n); SC = O(26)

    """
    from collections import Counter

    # Count freq:
    freq = sorted(Counter(s).items())

    half = []
    odd = ''
    # Add the 1st half to the arr:
    for c, x in freq:
        half.extend(c*(x//2))
        if x % 2:
            odd = c

    # Return 1st half + odd (if there) + 2nd half (reversed):
    # return ''.join(half) + odd + ''.join(half[::-1])
    return ''.join(chain(half, [odd], (half[i] for i in range(len(half)-1, -1, -1))))
    """

    # 0) Suboptimal (Sort): TC = O(n*log(n)); SC = O(n)
    # From:
    # https://leetcode.com/problems/smallest-palindromic-rearrangement-i/solutions/6644865/2-steps-simple-solution-clean-code-o-n-log-n
    # Shorter because it benefits from the input string already being sorted to a palindrome.

    half = sorted(s[:len(s)//2])
    # return ''.join(half) + (s[len(s)//2] if len(s) % 2 else '') + ''.join(half[::-1])
    return ''.join(chain(half,
                         [(s[len(s)//2] if len(s) % 2 else '')],
                         (half[i] for i in range(len(half)-1, -1, -1))))

    # Note:
    # Solutions `1.1` and `1.2` also work for the case when the given string is not sorted to already be a palindrome.
