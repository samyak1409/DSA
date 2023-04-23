"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
"""


def find_matrix(nums: list[int]) -> list[list[int]]:
    """"""

    # Process the elements in the array one by one in any order and only create a new row in the matrix when we cannot
    # put it into the existing rows.
    # We can simply iterate over the existing rows of the matrix to see if we can place each element.

    # 0) Brute-force (HashSet + Nested Loop): TC = O(n^2); SC = O(n) {storing all the elements}
    # Looking at the approach initially may seem like a linear one, but it's not.
    # Take the case when all nums are same.

    """
    ans = []

    for num in nums:  # O(n^2)
        for i in range(len(ans)):  # O(n)
            if num not in ans[i]:
                ans[i].add(num)
                break
        else:
            ans.append({num})  # O(1)

    # return [list(row) for row in ans]
    # or:
    yield from map(list, ans)
    """

    # 1) Optimal (Smart 👌 using HashMap): TC = O(n); SC = O(n)
    # Idea from:
    # https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/3368523/java-c-python-maximum-frequence
    # https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/3368321/counter

    from collections import Counter
    count = Counter()  # SC = O(n)
    ans = []

    for num in nums:  # O(n)
        try:  # EAFP
            ans[count[num]].append(num)  # try to append at the index if list is there
        except IndexError:
            ans.append([num])  # else add with a new list
        count[num] += 1  # update count

    return ans
