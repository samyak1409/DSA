"""
https://leetcode.com/problems/reverse-string
"""


def reverse_string(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    # 1) Optimal (Two Pointers): TC = O(n); SC = O(1)

    # 1.2) Using while loop:
    # https://leetcode.com/problems/reverse-string/solutions/3718521/easy-solution-with-simple-explanation
    """
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i, j = i+1, j-1
    """

    # 1.1) Using for loop:
    # https://leetcode.com/problems/reverse-string/solutions/669571/python-oneliner-two-pointers-explained
    """
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]  # (~i = -i-1)
    """

    # 2) Time-Optimal (Recursion): TC = O(n); SC = O(n) {recursion stack}
    # """
    # interviewer: "implement your own function, how about recursion"
    # *sweats*
    # This problem is a litmus test of whether a programmer will be replaced by chatgpt. This is not a test of our
    # syntax.
    # """
    # -https://leetcode.com/problems/reverse-string/description/comments/2022019

    # 2.1) Swap while recursing out:
    """
    # Recursive Function:
    def reverse(i: int = 0) -> None:
        if i < n//2:
            reverse(i=i+1)  # recurse in
            # While recursing out:
            s[i], s[~i] = s[~i], s[i]

    n = len(s)
    reverse()
    """

    # 2.2) Swap while recursing in:
    # Recursive Function:
    def reverse(i: int = 0) -> None:
        if i < n//2:
            s[i], s[~i] = s[~i], s[i]
            reverse(i=i+1)  # recurse in

    n = len(s)
    reverse()
