class Solution:
    def canJump(self, nums: [int]) -> bool:
        earliest_win = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= earliest_win:
                earliest_win = i

            print(i, earliest_win)

        return earliest_win == 0

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
