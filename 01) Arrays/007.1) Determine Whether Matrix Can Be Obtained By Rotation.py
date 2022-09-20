"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
"""


def find_rotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    """"""

    # What is the maximum number of rotations you have to check?
    # Is there a formula you can use to rotate a matrix 90 degrees?

    # 1) Brute-force = Optimal (Check & Rotate 4 Times): TC = O(n^2); SC = O(1)

    # Helper Function:
    def rotate() -> None:
        """https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/007%29%20Rotate%20Image.py"""
        # Transposing:
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # Mirroring on Y-axis:
        for i in range(n):
            mat[i].reverse()

    n = len(mat)
    for _ in range(4):
        # Check: 0°, 90°, 180°, 270°
        if mat == target:
            return True
        # Rotate 90° (clockwise): 90°, 180°, 270°, 360°
        rotate()  # O(n^2)

    # Extra Note: If mat != target after any ([0, 3] => 0°, 90°, 180°, 270°) number of rotations, mat will come be back
    # to its original orientation.

    # Also see:
    # https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss/1254089/C++-straightforward-solution-comparing-in-place
