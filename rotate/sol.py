class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        n = len(matrix)

        for r in range((n + 1) // 2):
            for c in range(n // 2):
                matrix[r][c], matrix[c][n-1-r], matrix[n-1-r][n-1-c], matrix[n-1-c][r] = matrix[n-1-c][r], matrix[r][c], matrix[c][n-1-r], matrix[n-1-r][n-1-c]

def print_matrix(matrix: [[int]]) -> None:
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')

        print()

sol = Solution()
m = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
m2 = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]
]
sol.rotate(m)
sol.rotate(m2)
print_matrix(m)
print_matrix(m2)

n = 4

(0, 1)
(1, 3)
(3, 2)
(2, 0)
