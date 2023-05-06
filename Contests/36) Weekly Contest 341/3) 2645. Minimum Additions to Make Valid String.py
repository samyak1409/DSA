"""
https://leetcode.com/problems/minimum-additions-to-make-valid-string
"""


def add_minimum(word: str) -> int:
    """"""

    # 1) Optimal (Smart One: Two Pointers + Circular/Cyclic String/Iteration): TC = O(n); SC = O(1)
    # Maintain a pointer on word and another pointer on string “abc”.
    # If the two characters that are being pointed to differ, Increment the answer and the pointer to the string “abc”
    # by one.

    base = 'abc'
    i = j = 0  # 2 pointers

    ans = 0

    while i < len(word):  # while not traversed `word`
        if word[i] != base[j]:  # if both chars are not the same
            ans += 1  # we need to add a char to `word`, so directly ++ans
        else:  # if same
            i += 1  # then we can just go ahead
        j = (j+1) % len(base)  # and we'll always go ahead in the base string
        # `% len(base)`: point to 0 again once it go out of bound

    return ans + ord(base[-1])-ord(word[-1])  # `+ ord(base[-1])-ord(word[-1])`: for when `word` doesn't end w/ a 'c'

    # 1.1) Just a different way of implementing:
    # https://leetcode.com/problems/minimum-additions-to-make-valid-string/solutions/3421831/java-c-python-easy-and-concise-with-explanation/comments/1865079

    """
    base = 'abc'
    ans = i = 0
    while True:
        for c in base:
            if word[i] == c:  # if same
                i += 1  # just move ahead
                if i == len(word):  # if traversed whole
                    return ans + ord(base[-1])-ord(c)  # `+ ord(base[-1])-ord(c)`: for when `word` doesn't end w/ a 'c'
            else:  # if not same
                ans += 1
    """

    # 2) Another Approach:
    # https://leetcode.com/problems/minimum-additions-to-make-valid-string/solutions/3421831/java-c-python-easy-and-concise-with-explanation
