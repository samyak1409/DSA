"""
https://leetcode.com/problems/product-of-array-except-self
"""


def product_except_self(nums: list[int]) -> list[int]:
    """"""

    # You must write an algorithm that runs in O(n) time and without using the division operation.
    # -1) Not Allowed (Calc. Total Product, Divide by Self One by One): TC = (n); SC = O(1)

    # -1.1) [WA]
    """
    from math import prod
    product = prod(nums)
    for num in nums:
        yield product // num
    """
    # Wait! The array can have zeroes too! And the impact of zero in product is destructive.
    # Check Example 2: Input: nums = [-1, 1, 0, -3, 3] Output: [0, 0, 9, 0, 0]
    # -1.2) [WA] We need one more variable which will store the product without zero(es):
    """
    product = product_without_0 = 1  # init with neutral val
    for num in nums:
        product *= num
        if num:
            product_without_0 *= num
    for num in nums:
        yield product//num if num else product_without_0
    """
    # WA 🤦 Input: [0, 0] Output: [1, 1] Expected: [0, 0]
    # So, after analysis, cases can be categorized in three types:
    # i) nums.count(0) == 0
    # ii) nums.count(0) == 1
    # iii) nums.count(0) >= 2
    # `-1.1)` was handling cases `i)`
    # `-1.2)` was handling cases `i)` & `ii)`
    # -1.3) Handles all the cases (`i)`, `ii)` & `iii)`):
    """
    match nums.count(0):
        case 0:
            from math import prod
            product = prod(nums)
            for num in nums:
                yield product // num
        case 1:
            product_without_0 = 1  # init with neutral val
            for num in filter(None, nums):
                product_without_0 *= num
            for num in nums:
                yield 0 if num else product_without_0
        case _:  # (>= 2)
            for i in range(len(nums)):
                yield 0
    """
    # See 😂:
    # Runtime: 210 ms, faster than 99.92% of Python3 online submissions for Product of Array Except Self.
    # Memory Usage: 20.7 MB, less than 99.39% of Python3 online submissions for Product of Array Except Self.

    # https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space/67603
    # https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C++Python-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach

    # 1) Optimal (Prefix & Suffix Product): TC = O(n); SC = O(n)
    #            nums:     1   2   3
    # prefix_products: 1   1   2
    # suffix_products:         6   3   1
    #            ans.:    1*6 1*3 2*1
    #          = ans.:     6   3   2

    """
    n = len(nums)
    prefix_products, suffix_products = [0]*n, [0]*n
    prefix_products[0] = suffix_products[-1] = 1
    for i in range(n-1):
        prefix_products[i+1] = prefix_products[i] * nums[i]
        suffix_products[~(i+1)] = suffix_products[~i] * nums[~i]
    for i in range(n):
        yield prefix_products[i] * suffix_products[i]
    """

    # Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra
    # space for space complexity analysis.)

    # NO! It can't be solved in O(1) SC (with O(n) TC), this is kind of STUPID when talking like "we can use the output
    # array to store bla bla bla", bro, it's called O(1) SC when you don't compulsorily need output to store, and you
    # can directly yield or print the output to the console. Here, can you? No you can't, you're being like "oh it's
    # O(1) SC, just let me return the output in form of an array..." 🤦

    # 1.1) Better to call it "Using only Single Array Storage": TC = O(n); SC = O(n)

    n = len(nums)
    suffix_products, suffix_products[-1] = [0]*n, 1
    for i in range(-1, -n, -1):
        suffix_products[i-1] = suffix_products[i] * nums[i]
    prefix_product = 1
    for i, num in enumerate(nums):
        yield prefix_product * suffix_products[i]
        prefix_product *= num
