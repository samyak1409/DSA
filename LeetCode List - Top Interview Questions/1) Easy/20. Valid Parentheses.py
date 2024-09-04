"""
https://leetcode.com/problems/valid-parentheses
"""


def is_valid(s: str) -> bool:
    """"""

    # 1) Optimal (Stack): TC = O(n); SC = O(n)

    if len(s) % 2:  # optimization: odd no. of brackets
        return False

    hm = {'(': ')', '{': '}', '[': ']'}
    st = []  # SC = O(n)

    for bracket in s:  # TC = O(n)

        if closing_bracket := hm.get(bracket):  # if bracket is opening bracket
            st.append(closing_bracket)  # push its closing to the stack (for future)

        else:
            if not st or bracket != st.pop():  # compare the closing bracket with the top of the stack
                return False

    return st == []  # if stack is not empty means some bracket is not closed
