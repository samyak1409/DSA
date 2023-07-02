"""
https://leetcode.com/problems/neighboring-bitwise-xor
"""


def does_valid_array_exist(derived: list[int]) -> bool:
    """"""

    # 1) Time-Optimal (Build the Original Arr and Verify): TC = O(n); SC = O(n)
    # Notice when the derived[i] = 0 or 1.
    #   derived[i] == 0 when original[i-1] == original[i]
    #   derived[i] == 1 when original[i-1] != original[i]
    # So, what we can do is, we can make the original array for n-1 elements, and then verify if it gives correct result
    # for the last element or not.
    # Check the comments below.

    """
    if len(derived) == 1:
        return not derived[0]
    
    original = [0]
    
    for i in range(len(derived)-1):
        original.append(1-original[-1] if derived[i] else original[-1])
    
    return original[-1] != original[0] if derived[-1] else original[-1] == original[0]
    """

    # Concise:

    """
    # Init the original arr w/ any first val:
    original = [0]

    # Then for n-1 elements from derived arr, fill original depending upon the val of derived[i]:
    for i in range(len(derived)-1):
        original.append(1-original[-1] if derived[i] else original[-1])
        # `1-original[-1]`: derived[i] == 1 so this element needs to be different from the last one
        # `original[-1]`: derived[i] == 0 so this element needs to be same as the last one

    # Check and return the result if last element verifies w/ the built original arr:
    return derived[-1] == original[-1] ^ original[0]
    """

    # 1.1) Optimal (Build the Original Arr (only saving the last val) and Verify): TC = O(n); SC = O(1)
    # Space optimized of above as we just need the prev element, not the whole original arr.

    """
    # Init prev_val w/ any val:
    prev_val = 0

    # Then for n-1 elements from derived arr, keep getting new prev_val depending upon the val of derived[i]:
    for i in range(len(derived)-1):
        prev_val = 1-prev_val if derived[i] else prev_val
        # `1-prev_val`: derived[i] == 1 so this element needs to be different from the last one
        # `prev_val`: derived[i] == 0 so this element needs to be same as the last one

    # Check and return the result if last element verifies w/ the built original arr:
    return derived[-1] == prev_val ^ 0
    """

    # Understand that from the original element, we are using each element twice to construct the derived array
    # The xor-sum of the derived array should be 0 since there is always a duplicate occurrence of each element.

    # 2) Optimal (Bit-Math): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/neighboring-bitwise-xor/solutions/3522095/java-c-python-sum-is-even
    # "original: A[0], A[1], .... A[n-1]
    # derived: A[0]^A[1], A[1]^A[2] .... A[n-1]^A[0]
    # xor(derived) = (A[0]^A[1])^(A[1]^A[2])^ .... ^(A[n-1]^A[0]) = 0
    # The necessary and sufficient condition for derived to have an original is xor(derived) == 0"

    """
    from functools import reduce
    from operator import xor
    return reduce(xor, derived) == 0
    """

    # "When original and derived is binary sequence, this equals to sum(derived) % 2 == 0."
    # Think why. 😁

    return sum(derived) % 2 == 0
