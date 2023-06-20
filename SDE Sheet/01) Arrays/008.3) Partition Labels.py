"""
https://leetcode.com/problems/partition-labels
"""


def partition_labels(s: str) -> list[int]:
    """"""

    # https://leetcode.com/problems/partition-labels/solution
    # https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation

    # https://leetcode.com/problems/partition-labels/solution/132107: "How about an approach using intervals. Compute
    # interval (start, end) for each letter [a-z], where start is first occurrence of letter, and end is last occurrence
    # of letter. Then we merge any overlapping intervals, and the resulting intervals can form the answer."
    # Me: Exactly! (Easier to sink it in.)

    # 1) Optimal (Form Intervals, Merge, Yield Size): TC = O(n); SC = O(1) {s consists of lowercase English letters.}

    # Forming Partitions as Intervals:
    '''
    first_index, last_index = {}, {}
    for i, char in enumerate(s):
        if char not in first_index.keys():
            first_index[char] = i  # add only once
        last_index[char] = i  # update everytime
    # intervals = [[a, b] for a, b in zip(first_index.values(), last_index.values())]
    intervals = list(map(list, zip(first_index.values(), last_index.values())))
    '''
    interval = {}
    for i, char in enumerate(s):
        if char not in interval.keys():
            interval[char] = [i, i]  # init interval of char
        else:
            interval[char][1] = i  # update interval (to be precise: interval's end)
    intervals = list(interval.values())  # now we only want the resultant intervals formed
    # print(intervals)  #debugging

    # Merging Overlapping Intervals in order to calculate final size of Partitions:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/008%29%20Merge%20Intervals.py
    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] <= prev[1]:  # => intervals are overlapping!
            prev[1] = max(prev[1], curr[1])  # merging
        else:
            yield prev[1]-prev[0]+1  # adding the non-overlapping intervals to the output
            prev = curr  # updating previous in order to check if it can be merged with the following interval
    yield prev[1]-prev[0]+1  # adding the last (overlapping/non-overlapping) interval to the output
