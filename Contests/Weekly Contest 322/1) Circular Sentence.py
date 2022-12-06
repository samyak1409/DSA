"""
https://leetcode.com/problems/circular-sentence
"""


def is_circular_sentence(sentence: str) -> bool:
    """"""

    # 1) Time-Optimal (Split Words): TC = O(n); SC = O(n)

    """
    if sentence[0] != sentence[-1]:
        return False

    words = sentence.split()
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True
    """

    # 2) Optimal (Without Splitting Words: Check letters around spaces!): TC = O(n); SC = O(1)
    # Check the first character and the last character of the sentence.
    # Check the character before the empty space and the character after the empty space.

    if sentence[0] != sentence[-1]:
        return False

    for i in range(len(sentence)):
        if sentence[i] == ' ' and sentence[i-1] != sentence[i+1]:
            return False
    return True
