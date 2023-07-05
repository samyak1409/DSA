"""
https://leetcode.com/problems/lexicographically-smallest-palindrome
"""


def make_smallest_palindrome(s: str) -> str:
    """"""

    # We can make any string a palindrome, by simply making any character at index i equal to the character at index
    # length-i-1 (using 0-based indexing).
    # To make it lexicographically smallest we can change the character with maximum ASCII value to the one with minimum
    # ASCII value.
    
    # 1) Optimal (Two Pointers + Greedy): TC = O(n); SC = O(n)
    # Intuition: We have to make the str palindrome, so, whenever s[i] != s[~i], they'd be needed to be equalized.
    # So, for equating them, the best method would be just making either one of them equal to the other. Because,
    # this is an optimization (minimization) problem where we've to minimize the no. of ops.
    # Now, also, we've to make the palindrome lexicographically smallest if there can form multiple palindromes w/ the
    # same no. of ops. So, applying greedy method here: we've to perform only one op to make one chr equal to other, so,
    # taking the smaller of the two would surely give the optimal ans!

    # Converting to list because str is immutable:
    arr = list(s)

    # Loop using two pointers:
    for i in range(len(arr)//2):
        '''
        if arr[i] != arr[~i]:
            if arr[i] < arr[~i]:
                arr[~i] = arr[i]
            else:  # (if arr[i] > arr[~i])
                arr[i] = arr[~i]
        '''
        # For less LOCs, just:
        arr[i] = arr[~i] = min(arr[i], arr[~i])

    # Return the ans back in str:
    return ''.join(arr)

    # Also, check the Python solution in
    # https://leetcode.com/problems/lexicographically-smallest-palindrome/solutions/3546745/java-c-python-two-pointers
    # 😂, Python is GOAT.
