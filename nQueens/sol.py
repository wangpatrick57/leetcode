class Solution:
    def inBounds(self, r, c):
        n = len(self._covered)

        return r >= 0 and c >= 0 and r < n and c < n

    def diagonal(self, r, c, dr, dc, inc):
        while self.inBounds(r, c):
            self._covered[r][c] += inc
            r += dr
            c += dc

    def changeQueen(self, r, c, add):
        n = len(self._covered)
        inc = 1 if add else -1

        for ci in range(n):
            self._covered[r][ci] += inc

        for ri in range(n):
            self._covered[ri][c] += inc

        self.diagonal(r, c, 1, 1, inc)
        self.diagonal(r, c, 1, -1, inc)
        self.diagonal(r, c, -1, 1, inc)
        self.diagonal(r, c, -1, -1, inc)
        self._solution[r][c] = 'Q' if add else '.'

    def getSolution(self):
        return [''.join(row) for row in self._solution]

    def printCovered(self):
        for row in self._covered:
            print(' '.join(map(str, row)))

    def getBlank(self, n):
        self._covered = []
        self._solution = []

        for _ in range(n):
            self._covered.append([0] * n)
            self._solution.append(['.'] * n)

    def isOpen(self, r, c):
        return self._covered[r][c] == 0

    def solveNQueens(self, n):
        self.getBlank(n)
        solutions = []
        self.recurse(0, 0, solutions)
        return solutions

    def recurse(self, r, startC, solutions):
        n = len(self._covered)

        if r == n:
            solutions.append(self.getSolution())
            return

        for c in range(startC, n):
            if self.isOpen(r, c):
                self.changeQueen(r, c, True)
                self.recurse(r + 1, 0, solutions)
                self.changeQueen(r, c, False)

if __name__ == '__main__':
    s = Solution()
    out = s.solveNQueens(0)
    print(out)
