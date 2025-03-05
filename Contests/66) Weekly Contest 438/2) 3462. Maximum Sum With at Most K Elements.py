"""
https://leetcode.com/problems/maximum-sum-with-at-most-k-elements
"""


def max_sum(grid: list[list[int]], limits: list[int], k: int) -> int:
    """"""

    # 1) Sub-optimal (Greedy, Counting Sort): TC = O(10**5 + m*n); SC = O(10**5 + m*n)
    # Intuition:
    # "0 <= grid[i][j] <= 10^5" implies that we can build an arr as a hm, where `i`: element, `arr[i]`: list of row
    # indices of element.
    # Then, we can be greedy, and iterate in reverse, and add to the answer as long as `limits[r]` allow.

    """
    # Edge case: `k` already 0 (return from here only avoiding calculating anything):
    if k == 0:
        return 0

    arr = [[] for _ in range(10**5 + 1)]  # arr as hm; (`+ 1` because 0-indexed); TC = SC = O(10**5)
    # Fill our arr: TC = SC = O(m*n)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            arr[grid[r][c]].append(r)

    ans = 0
    # Reverse iterate (Greedy): O(10**5 + m*n)
    for el in range(len(arr)-1, -1, -1):
        # Iterate on row indices of current element:
        for r in arr[el]:
            # If limit of current row left:
            if limits[r]:
                # Then we can add to the ans:
                ans += el
                limits[r] -= 1
                # Return as soon as we're done with `k` additions:
                if (k := k-1) == 0:
                    return ans
    """

    # 2) Optimal (Greedy, Sort): TC = O(m*n * log2(m*n)); SC = O(m*n)
    # Same as above, only difference is using normal sort instead of counting sort.

    """
    # Edge case: `k` already 0 (return from here only avoiding calculating anything):
    if k == 0:
        return 0

    arr = []  # `arr[i]`: (element, its row index)
    # Fill our arr: TC = SC = O(m*n)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            arr.append((grid[r][c], r))

    ans = 0
    # Reverse sort and iterate (Greedy): TC = O(m*n * log2(m*n)); SC = O(m*n)
    for el, r in sorted(arr, reverse=True):
        # If limit of current row left:
        if limits[r]:
            # Then we can add to the ans:
            ans += el
            limits[r] -= 1
            # Return as soon as we're done with `k` additions:
            if (k := k-1) == 0:
                return ans
    """

    # Hint 1: Sort each row in descending order and extract the top limits[i] elements.

    # 2.1) Optimal (Greedy, Sort):
    # https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/solutions/6458024/94-beats-c-python-solution-for-maximizing-grid-sum
    # Actually, better to not sort all the elements, but sort each row, extract out `limits[r]` no. of elements from
    # each row. And then sort.

    # 2.1.1) [TLE] Using "Merge k Sorted Arrays": TC = O(m*n*log(n)); SC = O(m*n)
    # Also, since we're sorting the rows anyway, better to not flatten out and sort all the elements, but we can sort
    # using those `m` sorted rows (of `limits[r]` len) we got like https://leetcode.com/problems/merge-sorted-array.
    # Basically this: https://leetcode.com/problems/merge-k-sorted-lists, difference being this is linked list version
    # like linked list version of "88. Merge Sorted Array" is https://leetcode.com/problems/merge-two-sorted-lists.
    # [TLE] - Looks like TC of "Merge k Sorted Arrays" isn't O(m*n), but O(m*n*m) or O(m*n*n)
    # (basically not O(n^2), but O(n^3)).

    """
    # Edge case: `k` already 0 (return from here only avoiding calculating anything):
    if k == 0:
        return 0

    rows = []  # `rows[i]`: `row`; `row[i]`: element
    # Fill our arr: TC = O(m * n*log(n)); SC = O(m*n)
    for r in range(len(grid)):
        rows.append(sorted(grid[r], reverse=True)[:limits[r]])
    # print(rows)  # debug

    # Now, using "merge k sorted arrays" to sort efficiently (flatten out `rows`): TC = O(m*n); SC = O(m*n)
    # Like in https://leetcode.com/problems/merge-sorted-array, we had two index pointers, here since the number of
    # sorted arrays are dynamic, we'd have an array of index pointers:
    # (Note that we're sorting in reverse since we want max first):
    indices = [0] * len(rows)
    arr = []  # `arr[i]`: element
    # Do while loop, would stop when we've added all the elements to `arr`:
    while True:
        max_el, row_i = float('-inf'), None  # `max_el`: next maximum el
        # `row_i`: index of the row from rows which had `max_el`
        # Now, compare all the `row[idx]` to know which is the next maximum el to be appended to `arr`:
        for (i, idx), row in zip(enumerate(indices), rows):
            if idx < len(row) and row[idx] > max_el:  # (`idx < len(row)`: avoid index out of bound)
                max_el, row_i = row[idx], i
        # When we've added all:
        if row_i is None:
            break
        # Add maximum to arr, and ++`indices[row_i]`:
        arr.append(rows[row_i][indices[row_i]])
        indices[row_i] += 1
    # print(arr)  # debug

    ans = 0
    # Iterate on biggest elements: O(m*n)
    for el in arr:
        # Since, we've only added the elements under limit to our arr, we can directly add to the ans:
        ans += el
        # Return as soon as we're done with `k` additions:
        if (k := k-1) == 0:
            return ans
    """

    # 2.1.2) Basic implementation (flattening out and sort all the added elements (under limit) together):
    # TC = O(m*n * log2(m*n)); SC = O(m*n)
    # [Note that TC of this is same as `2)` because it's the worst case TC.]

    # Edge case: `k` already 0 (return from here only avoiding calculating anything):
    if k == 0:
        return 0

    arr = []  # `arr[i]`: element
    # Fill our arr: TC = O(m * n*log(n)); SC = O(m*n)
    for r in range(len(grid)):
        arr.extend(sorted(grid[r], reverse=True)[:limits[r]])
    print(arr)  # debug

    ans = 0
    # Reverse sort and iterate (Greedy): TC = O(m*n * log2(m*n)); SC = O(m*n)
    for el in sorted(arr, reverse=True):
        # Since, we've only added the elements under limit to our arr, we can directly add to the ans:
        ans += el
        # Return as soon as we're done with `k` additions:
        if (k := k-1) == 0:
            return ans
