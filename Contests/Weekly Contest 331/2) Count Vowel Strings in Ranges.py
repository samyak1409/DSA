"""
https://leetcode.com/problems/count-vowel-strings-in-ranges
"""


def vowel_strings(words: list[str], queries: list[list[int]]) -> list[int]:
    """"""

    # 1) Optimal (Prefix Sum): TC = O(n); SC = O(n)
    # Precompute the prefix sum of strings that start and end with vowels.
    # Use unordered_set to store vowels.
    # Check if the first and last characters of the string are present in the vowels set.
    # Subtract prefix sum for range [l-1, r] to find the number of strings starting and ending with vowels.
    # https://leetcode.com/problems/count-vowel-strings-in-ranges/solutions/3143758/prefix-sum-array-very-simple-and-easy-to-understand-solution

    vowels = {'a', 'e', 'i', 'o', 'u'}

    s = 0
    prefix = [s]
    for word in words:
        '''
        if word[0] in vowels and word[-1] in vowels:
            s += 1
        prefix.append(s)
        '''
        # Shorter:
        '''
        s += word[0] in vowels and word[-1] in vowels
        prefix.append(s)
        '''
        # Shorter:
        prefix.append(s := s + (word[0] in vowels and word[-1] in vowels))
    # print(prefix)  #debugging

    for lt, rt in queries:
        yield prefix[rt+1]-prefix[lt]
