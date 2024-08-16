"""
https://leetcode.com/problems/generate-parentheses
"""


from collections.abc import Iterator


def generate_parenthesis(n: int) -> list[str]:

    # https://leetcode.com/problems/generate-parentheses/solution/#approach-2-backtracking:
    # TC = O(4^n) (https://leetcode.com/problems/generate-parentheses/solution/1036480;
    # https://leetcode.com/problems/generate-parentheses/solution/249179); SC = O(n)

    def generate(p: str, lt: int, rt: int) -> Iterator[str]:
        if len(p) == n*2:  # base condition -> p (of len n*2) formed
            yield p
        else:
            if lt < n:  # more open parentheses can be added
                yield from generate(p+'(', lt+1, rt)  # recursive call 1
            if rt < lt:  # parentheses to close left
                yield from generate(p+')', lt, rt+1)  # recursive call 2

    yield from generate('', 0, 0)
