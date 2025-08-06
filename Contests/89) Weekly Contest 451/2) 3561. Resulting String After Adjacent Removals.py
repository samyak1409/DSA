"""
https://leetcode.com/problems/resulting-string-after-adjacent-removals
"""


def resulting_string(s: str) -> str:
    """"""

    # What the actual f? Due to some brain glitch, stack didn't come to my mind during the contest. And without a stack,
    # I don’t think it’s possible to solve this efficiently.
    # Worst rank ever.
    # When re-attempted this after a few days, solved it in under 10 minutes.

    # 1) Optimal (Stack): TC = O(n); SC = O(n)

    st = []
    for c in s:
        # If st is not empty and st.top and curr char are "consecutive":
        if st and abs(ord(st[-1])-ord(c)) in (1, 25):
            st.pop()
        else:
            st.append(c)
    return ''.join(st)
