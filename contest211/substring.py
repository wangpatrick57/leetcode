class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_pos = dict()
        max_length = -1

        for i, c in enumerate(s):
            if c in last_pos:
                max_length = max(i - last_pos[c] - 1, max_length)
            else:
                last_pos[c] = i

        return max_length

sol = Solution()
print(sol.maxLengthBetweenEqualCharacters('mgntdygtxrvxjnwksqhxuxtrv'))
