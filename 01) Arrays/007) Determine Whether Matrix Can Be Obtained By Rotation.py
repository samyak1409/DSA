"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
"""


def find_rotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    """"""

    # From: https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/007%29%20Rotate%20Image.py

    # 1) Brute-force = Optimal (Rotate & Check 3 Times): TC = O(n^2); SC = O(1)

    if mat == target:  # 0° / 360°
        return True

    n = len(mat)
    for _ in range(3):  # 90°, 180°, 270°
        # Transposing:
        for i in range(n):  # O(n^2)
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # Mirroring on Y-axis:
        for i in range(n):  # O(n^2)
            mat[i].reverse()

        if mat == target:
            return True

    return False
