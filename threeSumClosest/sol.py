DEBUG = True

class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1

                    l += 1
                elif curr_sum > target:
                    while r >= 1 and nums[r] == nums[r - 1]:
                        r -= 1

                    r -= 1

        return closest_sum

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = [0, 1, 5, 10, 4, 5]
        print(sol.threeSumClosest(input, 18))
