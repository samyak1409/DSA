"""
https://leetcode.com/problems/design-spreadsheet
"""


# 1) Sub-optimal (Using 2D Array Data Structure):
# DS choice: Brute-force

"""
# Helper function:
def get_coords(cell: str) -> tuple[int, int]:  # TC = SC = O(1)
    # Return row, col indices from cell string:
    return int(cell[1:])-1, ord(cell[0])-ord('A')


class Spreadsheet:

    def __init__(self, rows: int):  # TC = SC = O(rows*26)
        # Init 2D arr:
        self.rows = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:  # TC = SC = O(1)
        r, c = get_coords(cell)
        self.rows[r][c] = value

    def resetCell(self, cell: str) -> None:  # TC = SC = O(1)
        # DRY: Re-use `setCell`:
        self.setCell(cell, value=0)

    def getValue(self, formula: str) -> int:  # TC = SC = O(1)
        sum_ = 0
        # Split the values, iterate on them:
        for cell_or_int in formula[1:].split('+'):
            # And add depending on if the val is a cell str or an int:
            if cell_or_int[0].isalpha():
                r, c = get_coords(cell=cell_or_int)
                sum_ += self.rows[r][c]
            else:
                sum_ += int(cell_or_int)
        return sum_
"""


# 2) Optimal (Using Hashmap):
# DS choice: Optimal

class Spreadsheet:

    def __init__(self, rows: int):  # TC = SC = O(1)
        # Init hashmap:
        self.hm = {}

    def setCell(self, cell: str, value: int) -> None:  # TC = SC = O(1)
        self.hm[cell] = value

    def resetCell(self, cell: str) -> None:  # TC = SC = O(1)
        # self.hm[cell] = 0
        # OR, DRY: Re-use `setCell`:
        self.setCell(cell, value=0)

    def getValue(self, formula: str) -> int:  # TC = SC = O(1)
        sum_ = 0
        # Split the values, iterate on them:
        for cell_or_int in formula[1:].split('+'):
            # And add depending on if the val is a cell str or an int:
            sum_ += self.hm.get(cell_or_int, 0) if cell_or_int[0].isalpha() else int(cell_or_int)
        return sum_


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
