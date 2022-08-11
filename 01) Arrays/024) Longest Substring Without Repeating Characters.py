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

    """
    last_index = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    longest_len = current_len = 0
    for index, char in enumerate(s):  # O(n)
        if char not in last_index:  # O(1)
            # increase the length of the substring by adding current char to the substring:
            current_len += 1
        else:
            # from the substring, remove the left most occurrence of the char which is repeated:
            current_len = index - last_index[char]
            # Remove all the previously saved_chars before new start index of current substring
            # (including the repeated char itself, so that from back (left most) it comes to front (right most)):
            for saved_char in last_index:  # O(1) because "s consists of English letters, digits, symbols and spaces."
                last_index.pop(saved_char)
                if saved_char == char:
                    break
        last_index[char] = index  # add to the hashmap
        longest_len = max(longest_len, current_len)  # calc the longest length
    return longest_len
    """
    # We don't really need to "Remove all the previously saved_chars before new start index of current substring"
    # We can just have a start_index and instead of removing previously saved chars we can just check if they come
    # before or after our new index.
    # Easy https://youtu.be/qtVh-XEpsJo?t=847
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/#approach-3-sliding-window-optimized
    last_index = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    start_index = 0
    longest_len = 0
    for current_index, char in enumerate(s):  # O(n)
        if (last := last_index.get(char)) is not None:  # O(1)
            # IMP: only setting the start_index to last_index[char]+1 if it is in the right of start_index
            #      else just ignoring because it means that we have already came ahead.
            start_index = max(start_index, last+1)
            # dry run the algo on input s = "abba" to understand what's going on.
        last_index[char] = current_index  # add/update to the hashmap
        longest_len = max(longest_len, current_index-start_index+1)  # calc the longest length
    return longest_len
