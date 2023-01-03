"""
https://leetcode.com/problems/count-pairs-of-similar-strings
"""


def similar_pairs(words: list[str]) -> int:
    """"""

    # 1) Optimal (HashMap): TC = O(n*n); SC = O(n)
    # How can you check if two strings are similar?
    # Use a hashSet to store the character of each string.

    from collections import Counter
    freq = Counter()  # for easy working
    ans = 0
    for word in words:  # O(n*n)
        chars = set(word)  # remove duplicates, TC = O(n)
        # We can't use set directly as dict keys because "unhashable type: 'set'", so we have to transform it.
        chars = tuple(sorted(chars))  # O(1) because "words[i] consist of only lowercase English letters."
        ans += freq[chars]  # count pairs
        freq[chars] += 1  # saving in the end satisfies `i < j`
    return ans

    # Read solutions using Bitmask (https://en.wikipedia.org/wiki/Mask_(computing)):
    # https://leetcode.com/problems/count-pairs-of-similar-strings/solutions/2923505/c-java-python3-frequency-table-mask
    # https://leetcode.com/problems/count-pairs-of-similar-strings/solutions/2923540/bitmask
