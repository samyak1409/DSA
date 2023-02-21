"""
https://leetcode.com/problems/count-anagrams
"""


def count_anagrams(s: str) -> int:
    """"""

    # 1) Optimal (Multiply number of unique perms of each word):
    # TC = O(n); SC = O(n) {how? take the case when `s` has only 1 word (with len == max_len i.e. 10^5)}
    # For each word, can you count the number of permutations possible if all characters are distinct?
    # How to reduce over-counting when letters are repeated?
    # The product of the counts of distinct permutations of all words will give the final answer.
    # "1. The basic idea is to multiply the number of ways to write each word.
    # 2. The number of ways to write a word of size n is n factorial i.e n!.
    # 3. For example "abc" -> "abc", "acb", "bac", "bca", "cab", "cba". total 6 ways = 3!.
    # 4. Here we want total unique count, so words like "aa" can be written in only 1 way. So we divide our ways by the
    # factorial of all repeating characters' frequencies.
    # 5. So we create a frequency array of word freq[].
    # 6. Now our formula is as follows: ways = n! / (freq[i]! * freq[i+1]! *...freq[n-1]!).
    # 7. So our overall answer is ways[i] * ways[i+1] * ... ways[n].
    # 8. But the problem here is that our answer can be a large number, so we have to return modulo 1e9+7.
    # 9. Well, that's not a big problem as we can just use cnt % mod for our answer, but here we have to use modulo for
    # every computation as numbers can be very large. In our formula: a= n!, b = (freq[i]! * freq[i+1]!... freq[n-1]! is
    # (a/b) % mod."
    # -https://leetcode.com/problems/count-anagrams/solutions/2947111/c-solution-math-with-explanation-each-step-in-detail
    # "PYTHON DEVELOPERS ARE IN LUCK DUE TO FACTORIAL AND LARGE INTEGER SUPPORT."
    # -https://leetcode.com/problems/count-anagrams/solutions/2947480/multiply-permutations

    from math import factorial, prod
    from collections import Counter

    ans = 1  # init with neutral prod
    for word in s.split():
        # Formula to find unique permutations: n! / r1! * r2! ... {r: repetition}
        ans *= factorial(len(word)) // prod(map(factorial, filter(lambda val: val > 1, Counter(word).values())))
        ans %= 1_000_000_007
    return ans
