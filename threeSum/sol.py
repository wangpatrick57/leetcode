DEBUG = True

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        sums = list()

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                this_sum = nums[i] + nums[l] + nums[r]

                inc_l = False
                inc_r = False

                if this_sum == 0:
                    sums.append([nums[i], nums[l], nums[r]])
                    inc_l = True
                    inc_r = True
                elif this_sum < 0:
                    inc_l = True
                else:
                    inc_r = True

                if inc_l:
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1

                    l += 1

                if inc_r:
                    while r >= 1 and nums[r - 1] == nums[r]:
                        r -= 1

                    r -= 1

        return sums

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = [0, 0, 0, -1, 1]
        print(f'answer = %s' %(sol.threeSum(input)))
