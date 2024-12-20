"""
https://leetcode.com/problems/minimize-string-length
"""


def minimized_string_length(s: str) -> int:
    """"""

    # This was a trick problem to waste time in reading long problem description and explanation.

    # 1) Optimal (HashSet): TC = O(n); SC = O(26) = O(1) {"`s` contains only lowercase English letters"}

    return len(set(s))
