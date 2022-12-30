"""
https://leetcode.com/problems/minimize-the-maximum-of-two-arrays
"""


def minimize_set(divisor1: int, divisor2: int, unique_cnt1: int, unique_cnt2: int) -> int:
    """"""

    if divisor1 > divisor2:
        return minimize_set(divisor2, divisor1, unique_cnt2, unique_cnt1)
    
    n = 0
    
    while unique_cnt1 != 0 or unique_cnt2 != 0:
        
        n += 1
        if unique_cnt1 > 0 and n % divisor1:
            unique_cnt1 -= 1
            continue
        if unique_cnt2 > 0 and n % divisor2:
            unique_cnt2 -= 1
    
    return n
