"""
https://leetcode.com/problems/implement-strstr
"""


def str_str(haystack: str, needle: str) -> int:

    # https://en.wikipedia.org/wiki/String-searching_algorithm; http://www-igm.univ-mlv.fr/~lecroq/string/index.html

    # Reference for time and space complexities: len(needle) = m; len(haystack) = n

    # 0) Built-in Method: TC = O(?); SC = O(?)

    """
    return haystack.find(needle)
    """

    # 1) Naive (char by char matching) [TLE]: TC = O((n-m)m); SC = O(1)

    """
    for i in range(len(haystack)-len(needle)+1):  # O(n-m)

        for j in range(len(needle)):  # O(m)
            if haystack[i+j] != needle[j]:  # O(1)
                break
        else:
            return i

    return -1
    """

    # 1.1) Naive (slicing and equating) [Accepted | 144 ms]: TC = O((n-m)m); SC = O(m)

    """
    for index in range(len(haystack)-len(needle)+1):  # O(n-m)

        if haystack[index:index+len(needle)] == needle:  # S = O(m) = T
            return index

    return -1
    """

    # 2) Knuth–Morris–Pratt Algorithm (https://youtu.be/V5-7GzOfADQ; https://youtu.be/GTJr8OvyEVQ):
    # TC = O(m+n); SC = O(m)

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
