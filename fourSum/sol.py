DEBUG = True

class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()

        sums = list()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    l_inc = False
                    r_inc = False

                    if curr_sum == target:
                        sums.append([nums[i], nums[j], nums[l], nums[r]])
                        l_inc = True
                        r_inc = True
                    elif curr_sum < target:
                        l_inc = True
                    else:
                        r_inc = True

                    if l_inc:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1

                        l += 1

                    if r_inc:
                        while r > l and nums[r] == nums[r - 1]:
                            r -= 1

                        r -= 1

        return sums

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input_list = [-4, -4, -3, -2, -1, 0, 1, 4, 8]
        target = 0
        print(sol.fourSum(input_list, target))
