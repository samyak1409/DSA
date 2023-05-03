"""
https://leetcode.com/problems/sum-of-distances
"""


def distance(nums: list[int]) -> list[int]:
    """"""

    # Can we use the prefix sum here?
    # For each number x, collect all the groups where x occurs, and calculate the prefix sum of the array.
    # For each occurrence of x, the groups to the right will be regular subtraction while the groups to the left will
    # be reversed subtraction.

    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    # 1) Optimal (HashMap; Maths): TC = O(n); SC = O(n)
    # The trick is to just calc. the relative change in the distance sum when going from the last index to the current
    # index.
    # (Successfully came up with this in the contest.)

    # Group the indices together using HashMap:
    groups = {}
    for i, num in enumerate(nums):
        if num in groups.keys():
            groups[num].append(i)
        else:
            groups[num] = [i]
    # print(groups)  #debugging

    ans = [0] * len(nums)  # init
    for indices in groups.values():  # (`indices`: indices having same nums)

        # Calc. the distance sum using loop (i.e. O(n)) for first index:
        m = len(indices)
        dist_sum = sum(abs(indices[0]-indices[i]) for i in range(1, m))  # init
        ans[indices[0]] = dist_sum  # save
        # Then calc. using maths (multiplication) (i.e. O(1)) for other indices:
        for i in range(1, m):
            dist_moved = indices[i] - indices[i-1]  # from previous index to current one
            dist_sum -= dist_moved * (m-i)  # distance decrease for m-i elements
            dist_sum += dist_moved * i  # distance increase for i elements
            ans[indices[i]] = dist_sum  # save

    return ans

    # https://leetcode.com/problems/sum-of-distances/solutions/3396067/same-question-on-leetcode-just-copy-paste-it-will-be-accepted
