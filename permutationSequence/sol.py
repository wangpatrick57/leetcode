# 1234
# 1243
# 1324
# 1342
# 1423
# 1432
# 21..
# 21..
# 23..
# 23..
# 24..
# 24..
# 31..
# 31..
# 32..
# 32..
# 33..
# 33..
# 41..
# 41..
# 42..
# 42..
# 43..
# 43..

# to find first digit, divide by factorial of one below n
# whatever first digit is, ignore that

class Solution:
    def getPermutation(self, n, k):
        return self.recurse(n, list(map(str, range(1, n + 1))), k - 1)

    def factorial(self, n):
        ans = 1

        for i in range(1, n + 1):
            ans *= i

        return ans

    def recurse(self, n, digits, k):
        assert n == len(digits)

        if n == 1:
            return str(digits[0])
        else:
            prev_fact = self.factorial(n - 1)
            index = k // prev_fact
            this_digit = digits[index]
            digits = digits[:index] + digits[index + 1:]
            remaining = self.recurse(n - 1, digits, k % prev_fact)
            return this_digit + remaining

if __name__ == '__main__':
    s = Solution()
    n = 1

    for i in range(1, s.factorial(n) + 1):
        print(s.getPermutation(n, i))
