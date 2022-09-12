class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        while n >= 5:
            n //= 5
            ans += n

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(0), '0')
    print(s.trailingZeroes(4), '0')
    print(s.trailingZeroes(5), '1')
    print(s.trailingZeroes(9), '1')
    print(s.trailingZeroes(10), '2')
    print(s.trailingZeroes(25), '6')
    print(s.trailingZeroes(99), '22')
