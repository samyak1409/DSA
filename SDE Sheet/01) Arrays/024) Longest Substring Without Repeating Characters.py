"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


def length_of_longest_substring(s: str) -> int:
    """"""

    # 0) Brute-force (Check all the Substrings using Nested Loop & HashSet):
    # TC = O(n^2); SC = O(k) {"s consists of English letters, digits, symbols and spaces."}

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

    # 1) Sub-Optimal (Sliding Window & HashMap): TC = O(n*k); SC = O(k)
    #                                            {"s consists of English letters, digits, symbols and spaces."}

    # 1.0) Complete basic version in which on occurrence of a duplicate character, we start again from
    #      last_index[duplicate_char]+1 (i.e. we go back), and clear the `last_index` hashmap. (TC & SC are same.)

    # 1.1) A little better version (in which we never go back):
    """
    last_index = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    longest_len = current_len = 0
    for index, char in enumerate(s):  # O(n)
        if char not in last_index:  # O(1)
            # increase the length of the substring by adding current char to the substring:
            current_len += 1
        else:
            # from the substring, remove the left-most occurrence of the char which is repeated:
            current_len = index - last_index[char]
            # Remove all the previously saved_chars before new start index of current substring
            # (including the repeated char itself, so that from back (left-most) it comes to front (right-most)):
            for saved_char in last_index.copy():  # O(k) {"s consists of English letters, digits, symbols and spaces."}
                last_index.pop(saved_char)
                if saved_char == char:
                    break
        last_index[char] = index  # add to the hashmap
        longest_len = max(longest_len, current_len)  # calc the longest length
    return longest_len
    """

    # We don't really need to "Remove all the previously saved_chars before new start index of current substring".
    # We can just have a start_index and instead of removing previously saved chars we can just check if they come
    # before or after our new index.

    # 2) Optimal (Optimized: Sliding Window & HashMap): TC = O(n); SC = O(k)
    #                                                   {"s consists of English letters, digits, symbols and spaces."}
    # Easy https://youtu.be/qtVh-XEpsJo?t=847
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/#approach-3-sliding-window-optimized

    last_index = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    start_index = 0
    longest_len = 0
    for curr_index, char in enumerate(s):  # O(n)
        if (last := last_index.get(char)) is not None:  # O(1)
            start_index = max(start_index, last+1)
            # IMP: Only setting the start_index to last_index[char]+1 if it is in the right of start_index
            #      else just ignoring because it means that we have already came ahead.
            # Dry run the algo on input s = "abba" to understand what's going on.
        longest_len = max(longest_len, curr_index-start_index+1)  # calc the longest length
        last_index[char] = curr_index  # add/update to the hashmap
    return longest_len


# Similar Questions:
# https://leetcode.com/problems/maximum-erasure-value
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up
# https://leetcode.com/problems/longest-nice-subarray
# https://leetcode.com/problems/optimal-partition-of-string
