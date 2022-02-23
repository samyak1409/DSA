"""
https://leetcode.com/problems/valid-parentheses/
"""


def isValid(s: str) -> bool:

    # Using Stack: TC = O(n); SC = O(n)

    if len(s) % 2:  # optimization if odd no. of brackets
        return False

    closed = {'(': ')', '{': '}', '[': ']'}  # helper
    stack = [None]  # added None so that stack doesn't underflow

    for bracket in s:

        # if type of current bracket == opened, push its closed type to the stack (for future equality-check)
        if bracket in closed.keys():  # closed.keys() = set of opened brackets
            stack.append(closed[bracket])

        else:  # (if type of current bracket == closed)
            # pop an element (top) from stack and compare it with current bracket (type of both = closed), if not equal, means invalid parentheses
            if bracket != stack.pop():
                return False

    return stack == [None]  # check whether the stack is back to its initial value, and return
