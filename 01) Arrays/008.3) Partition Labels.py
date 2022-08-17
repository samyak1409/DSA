"""
https://leetcode.com/problems/partition-labels
"""


def partition_labels(s: str) -> list[int]:
    """"""

    # 1) Optimal (Forming Intervals, Merging, Calculating): TC = O(n); SC = O(1)
    #                                                                  {"s consists of lowercase English letters."}

    # Forming Partitions as Intervals:
    first_index, last_index = {}, {}
    for i, char in enumerate(s):
        if char not in first_index.keys():
            first_index[char] = i
        last_index[char] = i
    partitions = [[a, b] for a, b in zip(first_index.values(), last_index.values())]
    # print(partitions)  #debugging

    # Merging Overlapping Partitions in order to calculate final size of partitions:
    # https://github.com/samyak1409/DSA/blob/7cbe5e00f474eb6a0aee5e0b58d66296a59604c3/01%29%20Arrays/008%29%20Merge%20Intervals.py#L41
    prev = partitions[0]
    for i in range(1, len(partitions)):
        curr = partitions[i]
        if curr[0] <= prev[1]:  # => partitions are overlapping!
            prev[1] = max(prev[1], curr[1])  # merging
        else:
            yield prev[1]-prev[0]+1  # adding the non-overlapping partitions to the output
            prev = curr  # updating previous in order to check if it can be merged with the following interval
    yield prev[1]-prev[0]+1  # adding the last (overlapping/non-overlapping) interval to the output

    # Also see: https://leetcode.com/problems/partition-labels/solution
    # https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation
    # https://leetcode.com/problems/partition-labels/discuss/1868842/JavaC%2B%2B-VISUALLY-EXPLAINEDDDDD%21%21
