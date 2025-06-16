"""
https://leetcode.com/problems/find-most-frequent-vowel-and-consonant
"""


def max_freq_sum(s: str) -> int:
    """"""

    # 1) Optimal (Freq Arr + Loop): TC = O(n); SC = O(26)

    freq = [0] * 26
    max_v = max_c = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Track the counts of all the letters:
    for c in s:
        freq[i:=ord(c)-ord('a')] += 1
        # If char is vowel, update vowel max, else consonant max:
        if c in vowels:
            max_v = max(max_v, freq[i])
        else:
            max_c = max(max_c, freq[i])
    return max_v + max_c

    # Comparison with the top voted solutions: https://chatgpt.com/share/684fbcae-a3bc-800a-82e5-8383d0f46382
