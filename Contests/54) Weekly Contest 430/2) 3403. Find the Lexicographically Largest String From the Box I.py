"""
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i
"""


def answer_string(word: str, num_friends: int) -> str:
    """"""

    # 1) Optimal (Greedy, Iterate):
    # Worst Case: TC = O(n^2); SC = O(n) {suppose word = 'c'*5000, num_friends = 2}
    # Avg Case: TC = O(n); SC = O(n)
    # Iterate on indices `i` where `word[i] == max(word)`, and consider the longest possible split (sub-str) starting
    # from `i`.
    # [Came up with myself]
    # Good question!
    # Observation 1: For "lexicographically-largest-string", length doesn't matter the most, but the first char:
    # 'z' > 'yz', implies ans. should start from char = `max(word)`.
    # Observation 2: There could be multiple occurrences of `max(word)`, e.g. ('zazy', 2). So, we need to consider all
    # the sub-strings starting from `max(word)`.

    # Edge case: num_friends == 1, e.g. ('gh', 1):
    if num_friends == 1:
        return word

    biggest_c = max(word)  # O(n)
    # Longest possible length of a split (sub-str) {such that "word is split into num_friends non-empty strings"}:
    longest_split_len = len(word) - num_friends + 1
    ans = ''
    # Iterate on word, and only consider when char == max(word):
    for i, c in enumerate(word):  # O(n)
        if c == biggest_c:
            ans = max(ans, word[i:i+longest_split_len])  # TC = SC = O(n)
            # `word[i:i+longest_split_len]`: starting with i, such that the len is as long as possible.
            # Max len is `longest_split_len`, but len could be < `longest_split_len` as well, e.g. ('aaz', 2).
    return ans
