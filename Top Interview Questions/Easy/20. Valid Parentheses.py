"""
https://leetcode.com/problems/valid-parentheses/
"""


def isValid(s: str) -> bool:

    # Using Stack: TC = O(n) = SC

    if len(s) % 2:  # optimization if odd number of brackets are there
        return False

    closed = {'(': ')', '{': '}', '[': ']'}
    stack = ['']  # adding one element so that stack is empty error don't occur

    for bracket in s:

        if closed.get(bracket):  # if type(bracket) = opened
            stack.append(closed[bracket])

        elif bracket != stack.pop():
            return False

    return stack == ['']
