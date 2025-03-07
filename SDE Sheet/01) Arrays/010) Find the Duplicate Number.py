"""
https://leetcode.com/problems/find-the-duplicate-number
"""


def find_duplicate(nums: list[int]) -> int:
    """You must solve the problem without modifying the array nums and uses only constant extra space."""

    # https://leetcode.com/problems/find-the-duplicate-number/solution
    # https://leetcode.com/problems/find-the-duplicate-number/discuss

    # 0.1) Brute-force (Sort and Traverse): TC = O(n*log(n)); SC = O(n)
    # Note: This approach uses extra space (sorting) so doesn't fulfill the problem requirement.
    # Since sorting will take O(n) space anyway, let's not modify the input array at least (let's not sort in place).

    """
    sorted_nums = sorted(nums)
    for i in range(len(nums)-1):
        if sorted_nums[i] == sorted_nums[i+1]:
            return sorted_nums[i]
    """

    # 0.2) Time-Optimal Brute-force (HashSet): TC = O(n); SC = O(n)
    # Note: This approach uses extra space (hashset) so doesn't fulfill the problem requirement.

    """
    hash_set = set()
    for num in nums:  # TC = O(n)
        if num in hash_set:  # already in; TC = O(1)
            return num
        hash_set.add(num)  # SC = O(n)
    """

    # (Can also use Array as HashMap (indices as keys).)

    # Follow up: Can you solve the problem in linear runtime complexity?

    # 1.1) [WA] Optimal (Maths: Sum of n terms): TC = O(n); SC = O(1)
    # Because nums can be = [2, 2, 2, 2, 2]
    # "Given an array of integers nums containing n+1 integers where each integer is in the range [1, n] inclusive."
    # doesn't mean array will have all numbers from 1 to n, and 1 number from the range repeating,
    # but means if the array has n+1 numbers, every number will be between 1 and n (inclusive)!!
    # This was to clarify that array would never be = e.g. [2, 3, 3, 10]; => n+1 = 4 => n = 3; but 10 is not in the
    # range [1, 3].

    """
    n = len(nums) - 1
    return sum(nums) - n*(n+1)//2
    """

    # 1.2) [WA] Optimal (Bit Manipulation: Using XOR): TC = O(n); SC = O(1)
    # Same reason as above.

    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans ^= nums[i] ^ i
    return ans
    """

    # 1.3) Optimal (Swap Numbers to Corresponding Indices): TC = O(n); SC = O(1)
    # Note: This algorithm modifies the input array.
    # https://leetcode.com/problems/find-the-duplicate-number/solution/#approach-42-array-as-hashmap-iterative

    """
    while nums[0] != nums[nums[0]]:
        # nums[0], nums[nums[0]] = nums[nums[0]], nums[0]  # ❌
        # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/02%29%20Linked%20List/033.1%29%20Swap%20Nodes%20in%20Pairs.py#L50-L58
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]  # ✅
    return nums[0]
    """

    # 1.4) Optimal (Negating Numbers): TC = O(n); SC = O(1)
    # Note: This algorithm modifies the input array TEMPORARILY.
    # https://leetcode.com/problems/find-the-duplicate-number/solution/#approach-3-negative-marking

    """
    for i in range(len(nums)):
        index = abs(nums[i])  # index to leave mark at; abs() because nums[i] can be a negated value
        if nums[index] < 0:  # value at `index` found negated => `index` (nums[i]) is the duplicate number!
            for j in range(i):  # turning the negated elements back positive; range(i) because elements were
                # negated till here only
                nums[abs(nums[j])] *= -1
            # print(nums)  #debugging
            return index
        nums[index] *= -1  # leaving mark
        # print(nums)  #debugging
    """

    # 1.5) Optimal (Floyd's Cycle Detection Algo): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/find-the-duplicate-number/solution/#approach-7-floyds-tortoise-and-hare-cycle-detection

    slow = fast = nums[0]  # start from start
    while True:  # imp: exit controlled (do-while) loop
        slow, fast = nums[slow], nums[nums[fast]]  # next, next of next
        if slow == fast:  # (=> cycle detected)
            break

    slow2 = nums[0]  # start (of array)
    while slow2 != slow:  # finding the start point of cycle
        slow2, slow = nums[slow2], nums[slow]  # next, next

    return slow2  # duplicate found

    # Why does this work? Why does cycle always form in the first place?
    # Take an example: nums = [1, 4, 3, 4, 2]
    #              (Indices:)  0  1  2  3  4
    # So, cycle will always form because of the SIMPLE FACT that if a number (4) is occurring more than 1 times {let it
    # be x}, this means it's there at x indices (1 & 3), and so simply implying that x numbers (1 & 3) will be pointing
    # to that particular number (4), thus making a cycle!
    #                                                        1 -> 4 -> 2 -> 3
    #                                                             ↑_________|

    # [Remarks] https://leetcode.com/problems/find-the-duplicate-number/editorial/comments/593262


# Similar Questions:
# https://leetcode.com/problems/first-missing-positive
# https://leetcode.com/problems/single-number
# https://leetcode.com/problems/linked-list-cycle-ii
# https://leetcode.com/problems/missing-number
# https://leetcode.com/problems/set-mismatch
