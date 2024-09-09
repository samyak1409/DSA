"""
https://leetcode.com/problems/implement-strstr
"""


def str_str(haystack: str, needle: str) -> int:
    """"""

    # Reading resources:
    # https://en.wikipedia.org/wiki/String-searching_algorithm; http://www-igm.univ-mlv.fr/~lecroq/string/index.html

    # -1) Not Allowed (Built-in):

    """
    return haystack.find(needle)
    """

    # 0) Brute-force (Char by char matching): TC = O((n-m)m); SC = O(1) {m: len(needle), n: len(haystack)}

    """
    for i in range(len(haystack)-len(needle)+1):  # O(n-m)
        for j in range(len(needle)):  # O(m)
            if haystack[i+j] != needle[j]:  # O(1)
                break
        else:
            return i
    return -1
    """

    # 0.1) Brute-force (Str Slicing): TC = O((n-m)m); SC = O(m) {m: len(needle), n: len(haystack)}

    """
    for index in range(len(haystack)-len(needle)+1):  # O(n-m)
        if haystack[index:index+len(needle)] == needle:  # SC = TC = O(m)
            return index
    return -1
    """

    # 1) Optimal (Knuth–Morris–Pratt (KMP) Algorithm): TC = O(m+n); SC = O(m) {m: len(needle), n: len(haystack)}
    # NOTE: IT'S EASY!! CHECK IMPLEMENTATION `1.2)`.

    # Abdul Bari - https://youtu.be/V5-7GzOfADQ
    # Tushar Roy - https://youtu.be/GTJr8OvyEVQ (Pt.1), https://youtu.be/KG44VoDtsAA (Pt.2)
    # 1.1) This implementation use +1 & -1 indices:
    """
    if len(haystack) < len(needle):  # optimization
        return -1
    
    # Step 1) Preprocessing:
    lps_arr = [0]  # LPS - the Longest Prefix which is same as some Suffix; 0 for 1st char because it's the FIRST char
    p, s = 0, 1  # prefix suffix comparison start indices
    while s < len(needle):  # while we have not reached at the end of the string
        if needle[s] != needle[p]:  # char not matched
            if p == 0:  # no more prefix possible
                lps_arr.append(0)  # suffix not same as any prefix
                s += 1  # move suffix index to next
            else:
                p = lps_arr[p-1]  # move p (prefix index) like this
        else:
            lps_arr.append(p+1)  # add (prefix index + 1)
            # Increment both s and p:
            s += 1
            p += 1
    # print(lps_arr)  #debugging

    # Step 2) Main Searching:
    i = j = 0  # haystack and needle start indices
    while i < len(haystack) and j < len(needle):  # while any of them have NOT reached at the end
        if haystack[i] != needle[j]:  # char not matched
            if j == 0:  # already at needle's start
                i += 1  # increment in haystack
            else:
                j = lps_arr[j-1]  # start matching with prefix (THIS IS THE MAIN OPTIMIZATION OF KMP)
        else:
            # Increment both i and j:
            i += 1
            j += 1

    return i-len(needle) if (j == len(needle)) else -1  # (j == len(needle)) => needle found in haystack
    """

    # 1.2) This implementation does not use +1 & -1 indices (result stays the same):
    if len(haystack) < len(needle):  # optimization
        return -1

    # Preprocessing (Building LPS/Pi Table):
    # LPS: Longest Prefix which is same as suffix for a particular substr.
    # It's used to track if a particular substr is there in the past / left side.
    # This is the main thing which helps in the optimization of this fast str search algo.
    lps = [0]  # `lps[i]` is the index in the needle from where we need to start matching again in case of following
    #            mismatch: `needle[i] != haystack[j]`
    i, j = 0, 1
    while j < len(needle):
        lps.append(i)  # `i`: len of "LPS" for curr substr `needle[:j+1]`
        # Now, we need to check if match is there, if not, we need to make `i` = `lps[i]` and not directly `0`
        #     - Why? -> Try running on testcase to know: haystack = "aabaaabaaac", needle = "aabaaac"
        # And check again if match is there, and repeat until `i != 0`, because lps[0] is 0, so it'd become inf loop.
        while needle[j] != needle[i] and i != 0:
            i = lps[i]
        # We'd exit above when either match is occurred, or `i` became `0`, in former case, we'd ++i:
        if needle[j] == needle[i]:
            i += 1
        # And ++j anyways:
        j += 1
    # V.Imp: Check the output for understanding:
    print(lps)  # debugging

    # Main (Searching):
    i = j = 0
    while j < len(haystack):
        if needle[i] == haystack[j]:  # if char match
            i += 1
            j += 1  # inc both
            if i == len(needle):  # and check if the answer is found
                return j - len(needle)
        else:  # if not match
            if i != 0:  # when `i` is not already at `0` (because lps[0] is 0)
                i = lps[i]  # move `i` to `lps[i]` for trying to "resume" matching from a prev char in needle
            else:
                j += 1  # if `i` is at `0`, then we need to ++j
                # (now we're basically "restart" matching from the very first char of needle

    return -1

    # GOOD TEST CASES (1st line - haystack, 2nd line - needle):
    # "acacabacacabacacabacacac"
    # "acacabacacabacacac"
    # "aabaaabaaac"
    # "aabaaac"
    # "aaabaaabbbabaa"
    # "babb"
    # "adcadcaddcadde"
    # "adcadde"
    # "bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa"
    # "bbabba"
    # "ababcaababcaabc"
    # "ababcaabc"
