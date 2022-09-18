"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank
"""


def number_of_beams(bank: list[str]) -> int:
    """"""

    # 1) Brute-force = Optimal (Traverse and Add): TC = O(m*n); SC = O(1)
    # https://leetcode.com/problems/number-of-laser-beams-in-a-bank/discuss/1660943/Python3-Java-C++-Simple-O(mn)

    devices_prev = 0  # init; device count last time
    beams = 0
    for floor in bank:  # traverse every floor one by one
        if devices := floor.count('1'):  # if a floor have at least one device then laser beam(s) should be formed
            beams += devices_prev * devices  # add beams
            devices_prev = devices  # save current device count for future
    return beams
