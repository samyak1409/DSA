"""
https://leetcode.com/problems/ransom-note
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
    """"""

    # 1) Optimal (Save Counts in HashMap): TC = O(n); SC = O(1) {"consist of lowercase English letters only."}
    # Video Explanation:
    # https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4427

    """
    if len(ransom_note) > len(magazine):  # optimization
        return False

    from collections import Counter

    src = Counter(magazine)

    for char, freq in Counter(ransom_note).items():

        if freq > src[char]:
            return False

    return True
    """

    # Counters support rich comparison operators:
    # https://leetcode.com/problems/ransom-note/solutions/85837/o-m-n-one-liner-python
    # https://docs.python.org/3.11/library/collections.html#collections.Counter:~:text=Counters%20support%20rich%20comparison%20operators%20for%20equality%2C%20subset%2C%20and%20superset%20relationships%3A%20%3D%3D%2C%20!%3D%2C%20%3C%2C%20%3C%3D%2C%20%3E%2C%20%3E%3D.

    if len(ransom_note) > len(magazine):  # optimization
        return False

    from collections import Counter

    return Counter(ransom_note) <= Counter(magazine)
