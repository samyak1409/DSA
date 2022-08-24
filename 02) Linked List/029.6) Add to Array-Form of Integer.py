"""
https://leetcode.com/problems/add-to-array-form-of-integer
"""


def add_to_array_form(num: list[int], k: int) -> list[int]:
    """"""

    # 0) Brute-force (Type Casting): TC = O(n) {n = len(num)}; SC = O(1)

    """
    return list(map(int, str(int(''.join(map(str, num))) + k)))  # list (to str) to int, add ints, int (to str) to list
    """

    # 1) Optimal (Take k itself as a Carry): TC = O(n); SC = O(n) {n = len(num)}
    # https://leetcode.com/problems/add-to-array-form-of-integer/solution
    # https://leetcode.com/problems/add-to-array-form-of-integer/discuss/234488/JavaC%2B%2BPython-Take-K-itself-as-a-Carry

    for i in range(-1, -len(num)-1, -1):
        k, num[i] = divmod(num[i]+k, 10)  # x//y, x%y
        if not k:  # if carry over => add done (e.g. when num = [1,2,0,0], k = 34)
            break
    while k:  # consider case (num=[0], k=10000)
        num.insert(0, k % 10)  # insert LSB at arr start
        k //= 10
    return num
