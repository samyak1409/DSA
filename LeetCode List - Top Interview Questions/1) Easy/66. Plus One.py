"""
https://leetcode.com/problems/plus-one
"""


def plus_one(digits: list[int]) -> list[int]:

    # 1) Amateur: TC = O(n); SC = O(1)

    """
    plus_one = int(''.join(map(str, digits))) + 1

    # return list(map(int, str(plus_one)))
    # or:
    yield from map(int, str(plus_one))
    """

    # 2) Standard: TC = O(n); SC = O(1)

    for i in range(len(digits) - 1, -1, -1):  # (reverse traversal)

        if digits[i] != 9:  # addition without carry
            digits[i] += 1
            break  # done

        else:  # addition with carry

            if i != 0:  # digits[i] is not MSB
                digits[i] = 0
                # and then for loop continues

            else:  # digits[i] is MSB
                digits[i] = 1
                digits.append(0)  # add a 0 to the end
                # and then digits is returned (this was the last iteration)

    return digits

    # Also read: https://leetcode.com/problems/plus-one/discuss/24082/My-Simple-Java-Solution
