"""
https://leetcode.com/problems/categorize-box-according-to-criteria
"""


def categorize_box(length: int, width: int, height: int, mass: int) -> str:
    """"""

    # 1) Brute-force = Optimal (Use conditional statements to find the right category of the box.): TC = O(1); SC = O(1)

    category = ''
    # The box is "Bulky" if:
    # Any of the dimensions of the box is greater or equal to 104.
    # Or, the volume of the box is greater or equal to 109.
    if length >= 10**4 or width >= 10**4 or height >= 10**4 or length*width*height >= 10**9:
        category += 'Bulky'
    # If the mass of the box is greater or equal to 100, it is "Heavy".
    if mass >= 100:
        category += 'Heavy'

    # If the box is both "Bulky" and "Heavy", then its category is "Both".
    if category == 'BulkyHeavy':
        return 'Both'
    # If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
    if category == '':
        return 'Neither'
    # If the box is "Bulky" but not "Heavy", then its category is "Bulky".
    # If the box is "Heavy" but not "Bulky", then its category is "Heavy".
    return category
