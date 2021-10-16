"""
https://leetcode.com/problems/generate-parentheses/
"""


from typing import List


def generateParenthesis(n: int) -> List[str]:

    # https://leetcode.com/problems/generate-parentheses/solution/#approach-2-backtracking: TC = O(4^n) (https://leetcode.com/problems/generate-parentheses/solution/1036480; https://leetcode.com/problems/generate-parentheses/solution/249179); SC = O(n)

    def generate(p, l, r):
        if len(p) == n*2:  # base condition -> p (of len n*2) formed
            yield p
        else:
            if l < n:  # more open parentheses can be added
                yield from generate(p+'(', l+1, r)  # recursive call 1
            if r < l:  # parentheses to close left
                yield from generate(p+')', l, r+1)  # recursive call 2

    yield from generate('', 0, 0)
