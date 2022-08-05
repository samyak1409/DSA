"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


def length_of_longest_substring(s: str) -> int:
    """"""

    # 0) Brute-force (Nested Loop & HashSet): TC = O(n^2); SC = O(1) because of Q. constraint
    #                                                      "s consists of English letters, digits, symbols and spaces."

    """
    n = len(s)
    longest_len = 0
    for i in range(n):
        occurred = set()  # for O(1) lookup and storing unique elements
        current_len = 0
        for j in range(i, n):
            char = s[j]
            if char not in occurred:
                current_len += 1
                occurred.add(char)
            else:  # when a char is repeated
                break  # start the loop with next starting
        longest_len = max(longest_len, current_len)
    return longest_len
    """

    # 1) Optimal (Sliding Window & HashMap): TC = O(n); SC = O(1) because of Q. constraint
    #                                                   "s consists of English letters, digits, symbols and spaces."

    occurred = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    longest_len = current_len = 0
    for index, char in enumerate(s):  # O(n)
        if char not in occurred:  # O(1)
            # increase the length of the substring by adding current char to the substring:
            current_len += 1
        else:
            # from the substring, remove the left most occurrence of the char which is repeated:
            current_len = index - occurred[char]
            # Remove all the previously saved_chars before new start index of current substring
            # (including the repeated char itself, so that from back (left most) it comes to front (right most)):
            for saved_char in occurred:  # O(1) because "s consists of English letters, digits, symbols and spaces."
                occurred.pop(saved_char)
                if saved_char == char:
                    break
        occurred[char] = index  # add to the hashmap
        longest_len = max(longest_len, current_len)  # calc the longest length
    return longest_len
