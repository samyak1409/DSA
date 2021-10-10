"""
https://leetcode.com/problems/implement-strstr/
"""


def strStr(haystack: str, needle: str) -> int:

    # Brute Force: TC = O(nm); SC = O(1)

    """
    if len(needle) > len(haystack):
        return -1

    if haystack == '':
        return 0

    for i in range(0, len(haystack)-len(needle)+1):  # O(n)

        for n, h in zip(needle, haystack[i:]):  # O(m)
            if n != h:
                break
        else:
            return i

    return -1
    """

    # Using Built-in Method: TC = O(n); SC = O(1)

    # return haystack.find(needle)

    # Knuth–Morris–Pratt Algorithm (https://youtu.be/GTJr8OvyEVQ; https://youtu.be/V5-7GzOfADQ): TC = O(m+n); SC = O(m)

    # Step 1) Preprocessing:

    lps_arr = [0]  # LPS- longest prefix which is same as some suffix; 0 for 1st char because it's the FIRST char
    p, s = 0, 1  # prefix suffix comparison start indices

    while s < len(needle):  # while we not reached the end of the string

        if needle[s] != needle[p]:  # char not matched

            if p == 0:  # no more prefix possible
                lps_arr.append(0)  # suffix not same as any prefix
                s += 1  # move to next suffix
            else:
                p = lps_arr[p-1]  # move p (prefix index) like this

        else:
            lps_arr.append(p+1)  # add prefix index + 1
            # Increment both s and p:
            s += 1
            p += 1

    print(lps_arr)  # debug

    # Step 2) Main Searching:

    i = j = 0  # haystack and needle start indices

    while i < len(haystack) and j < len(needle):  # while any of them has not reached the end

        if haystack[i] != needle[j]:  # char not matched

            if j == 0:  # already at needle's start
                i += 1  # increment in haystack
            else:
                j = lps_arr[j-1]  # start matching with prefix (THIS IS THE MAIN OPTIMIZATION OF KMP)

        else:
            # Increment both i and j:
            i += 1
            j += 1

    return i-len(needle) if j == len(needle) else -1
