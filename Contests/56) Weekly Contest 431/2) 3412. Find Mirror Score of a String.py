"""
https://leetcode.com/problems/find-mirror-score-of-a-string
"""


def calculate_score(s: str) -> int:
    """"""

    # 1) Optimal (Iterate, HashMap, Stack): TC = O(n); SC = O(n) {n == len(s)}

    hm = {chr(i): [] for i in range(ord('a'), ord('z')+1)}  # key: letter; value: stack of indices "j"
    ans = 0
    # Iterate:
    for i, letter in enumerate(s):
        # Get the mirror of `letter`, and check in `hm` if mirror's stack has at least an index:
        if stack := hm.get(chr(ord('z')-(ord(letter)-ord('a')))):
            # If yes, remove j ("closest unmarked index") from the stack, "add the value i - j to the total score":
            ans += i - stack.pop()
        else:
            # Else, just save the current index for future:
            hm[letter].append(i)
    return ans
