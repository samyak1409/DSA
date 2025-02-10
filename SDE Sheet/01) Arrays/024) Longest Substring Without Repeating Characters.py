"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


def length_of_longest_substring(s: str) -> int:
    """"""

    # 0) Brute-force (Check all the Substrings using Nested Loop & HashSet):
    # TC = O(n^2); SC = O(k) {"s consists of English letters, digits, symbols and spaces."}

    """
    ans = 0
    for i in range(n:=len(s)):
        seen = set()  # for O(1) lookup and storing unique elements
        curr_len = 0
        for j in range(i, n):
            c = s[j]
            if c not in seen:
                curr_len += 1
                seen.add(c)
            else:  # when a char is repeated
                break  # start the loop with next starting
        ans = max(ans, curr_len)
    return ans
    """

    # 1) Sub-Optimal (Sliding Window & HashMap): TC = O(n*k); SC = O(k)
    #                                            {"s consists of English letters, digits, symbols and spaces."}

    # 1.0) Complete basic version in which on occurrence of a duplicate character, we start again from
    #      last_index[duplicate_char]+1 (i.e. we go back), and clear the `last_index` hashmap. (TC & SC are same.)

    # 1.1) A little better version (in which we never go back):
    """
    last_index = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    ans = curr_len = 0
    for i, c in enumerate(s):  # O(n)
        if c not in last_index:  # O(1)
            # increase the length of the substring by adding current char to the substring:
            curr_len += 1
        else:
            # from the substring, remove the left-most occurrence of the char which is repeated:
            curr_len = i - last_index[c]
            # Remove all the previously saved_chars before new start index of current substring
            # (including the repeated char itself, so that from back (left-most) it comes to front (right-most)):
            for saved_char in last_index.copy():  # O(k) {"s consists of English letters, digits, symbols and spaces."}
                last_index.pop(saved_char)
                if saved_char == c:
                    break
        last_index[c] = i  # add to the hashmap
        ans = max(ans, curr_len)  # calc the longest length
    return ans
    """

    # We don't really need to "Remove all the previously saved_chars before new start index of current substring".
    # We can just have a start_index and instead of removing previously saved chars we can just check if they come
    # before or after our new index.

    # 2) Optimal (Optimized: Sliding Window & HashMap): TC = O(n); SC = O(k)
    #                                                   {"s consists of English letters, digits, symbols and spaces."}
    # Easy https://youtu.be/qtVh-XEpsJo?t=847
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/#approach-3-sliding-window-optimized

    """
    last_index = {}  # for O(1) lookup and storing unique elements (dict keys must be unique)
    start_index = 0
    ans = 0
    for curr_index, c in enumerate(s):  # O(n)
        if (last := last_index.get(c)) is not None:  # O(1)
            start_index = max(start_index, last+1)
            # IMP: Only setting the start_index to last_index[c]+1 if it is in the right of start_index
            #      else just ignoring because it means that we have already came ahead.
            # Dry run the algo on input s = "abba" to understand what's going on.
        ans = max(ans, curr_index-start_index+1)  # calc the longest length
        last_index[c] = curr_index  # add/update to the hashmap
    return ans
    """
    # Or:
    hm = {}  # (char: latest index)
    ans = 0
    i = -1
    for j, c in enumerate(s):
        # If we've seen `c` before, and it's after the curr start index `i` (of curr longest substr without repeating
        # chars), then move the curr start index to it:
        if (last := hm.get(c)) is not None and last >= i+1:  # (`i+1` instead of `i` because we're keeping the start
            # index 1 less, so that we can just `j-i` instead of `j-i+1`)
            i = last
        ans = max(ans, j-i)
        hm[c] = j  # insert/update latest index of a char
    return ans

# Similar Questions:
# https://leetcode.com/problems/maximum-erasure-value
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up
# https://leetcode.com/problems/longest-nice-subarray
# https://leetcode.com/problems/optimal-partition-of-string
