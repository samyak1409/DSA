"""
https://leetcode.com/problems/remove-letter-to-equalize-frequency
"""


def equal_frequency(word: str) -> bool:
    """"""

    # No.1 Least Accepted Easy Question
    # (https://leetcode.com/problemset/all/?difficulty=EASY&sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkFDX1JBVEUifV0%3D)

    # Side-note:
    # https://leetcode.com/problems/remove-letter-to-equalize-frequency/solutions/2646539/this-problem-wasn-t-easy

    # Brute force all letters that could be removed.
    # Use a frequency array of size 26.

    # 1) Brute-force = Optimal (Remove every letter one by one and Check):
    # TC = O(n + k^2); SC = O(k)
    # n == len(word); k == len(set(word)), but as "word consists of lowercase English letters only", max(k) == 26
    # => TC = O(n + 26^2) = O(n); SC = O(26) = O(1)
    #
    # (2nd in:
    # https://leetcode.com/problems/remove-letter-to-equalize-frequency/solutions/2646851/easy-to-understand-python)

    """
    from collections import Counter

    freq = Counter(word)  # O(n)

    for letter in freq.keys():  # loop on unique letters; O(k * k)

        freq[letter] -= 1  # remove letter

        # Check if after removing that particular letter, freq is = or not:
        # (Note that `filter` because if freq == 0, that letter is completely removed and won't be considered in the 
        # word.)
        if len(set(filter(None, freq.values()))) == 1:  # O(k)
            return True

        freq[letter] += 1  # add back for next iteration

    return False
    """

    # 2) Optimal (Greedy: Remove a letter from the least & most freq and Check):
    # TC = O(n + k*log(k)); SC = O(k)
    # n == len(word); k == len(set(word)), but as "word consists of lowercase English letters only", max(k) == 26
    # => TC = O(n + 26*log(26)) = O(n); SC = O(26) = O(1)
    #
    # We can observe that we can be greedy here, and try removing one letter from the least frequency, and one letter
    # from the most frequency.
    # Equalizing frequencies can only and only be possible by removing either of those, try some examples to see.

    from collections import Counter

    # Sort the frequencies of (unique) letters:
    freq = sorted(Counter(word).values())  # O(n + k*log(k))
    # print(freq)  #debugging

    freq[0] -= 1  # remove a letter from the least freq
    if len(set(filter(None, freq))) == 1:  # O(k)
        return True

    freq[0] += 1  # add back for following
    freq[-1] -= 1  # remove a letter from the most freq
    return len(set(filter(None, freq))) == 1  # O(k)
