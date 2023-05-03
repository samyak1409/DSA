"""
https://leetcode.com/problems/intervals-between-identical-elements
"""


def get_distances(arr: list[int]) -> list[int]:
    """"""

    # For each unique value found in the array, store a sorted list of indices of elements that have this value in the
    # array.
    # One way of doing this is to use a HashMap that maps the values to their list of indices. Update this mapping as
    # you iterate through the array.
    # Process each list of indices separately and get the sum of intervals for the elements of that value by utilizing
    # prefix sums.
    # For each element, keep track of the sum of indices of the identical elements that have come before and that will
    # come after respectively. Use this to calculate the sum of intervals for that element to the rest of the elements
    # with identical values.

    # https://leetcode.com/problems/intervals-between-identical-elements/solutions

    # {FROM `2) 2615. Sum of Distances.py`}

    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    # 1) Optimal (HashMap; Maths): TC = O(n); SC = O(n)
    # The trick is to just calc. the relative change in the distance sum when going from the last index to the current
    # index.

    # Group the indices together using HashMap:
    groups = {}
    for i, num in enumerate(arr):
        if num in groups.keys():
            groups[num].append(i)
        else:
            groups[num] = [i]
    # print(groups)  #debugging

    ans = [0] * len(arr)  # init
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
