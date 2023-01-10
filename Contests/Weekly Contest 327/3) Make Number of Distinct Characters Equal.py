"""
https://leetcode.com/problems/make-number-of-distinct-characters-equal
"""


def is_it_possible(word1: str, word2: str) -> bool:
    """"""

    # Create a frequency array of the letters of each string.
    # There are 26*26 possible pairs of letters to swap. Can we try them all?
    # Iterate over all possible pairs of letters and check if swapping them will yield two strings that have the same
    # number of distinct characters. Use the frequency array for the check.

    # 1) Brute-force = Optimal (Try Every Combination): TC = O(m+n + 26*26) = O(m+n); SC = O(26+26) = O(1)
    # https://leetcode.com/problems/make-number-of-distinct-characters-equal/solutions/3016989/c-java-python3-freq-table

    # NOTE THAT WE COMPULSORILY NEED TO SWAP ONCE (AND ONLY ONCE).

    from collections import Counter

    freq1, freq2 = Counter(word1), Counter(word2)  # TC = O(m+n); SC = O(26+26)
    distinct1, distinct2 = len(freq1), len(freq2)

    # Helper Function:
    def diff(d1: int = distinct1, d2: int = distinct2) -> int: return abs(d1-d2)

    if diff() >= 3:  # optimization: impossible to make them equal with exactly one move
        # e.g.: word1 = 'abcd', word2 = 'aaaa'
        return False

    for chr1, cnt1 in freq1.items():  # O(26*26)
        for chr2, cnt2 in freq2.items():  # O(26)
            if chr1 == chr2:
                if diff() == 0:  # if chr1 == chr2 and distinct counts are equal, we can return True
                    return True  # because if we swap => one required swap complete with equal distinct counts
            else:  # (because if chr1 == chr2, swapping won't make the distinct counts change)
                # Not swapping actually, just modifying the distinct count which will be if swapped:
                if diff(distinct1-(cnt1 == 1)+(freq1[chr2] == 0), distinct2-(cnt2 == 1)+(freq2[chr1] == 0)) == 0:
                    # `-(cnt1 == 1)` & `-(cnt2 == 1)`: if the char that we moved to the other word was only there a
                    # single time in word, distinct count of word will ↓ by 1
                    # `+(freq1[chr2] == 0)` & `+(freq2[chr1] == 0)`: if the char that we got from the other word was not
                    # there in word, distinct count of word will ↑ by 1
                    return True
