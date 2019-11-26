# [0, 1, 2, 3, 4, 5, 6] right
# [6, 0, 1, 2, 3, 4, 5] left
# [5, 6, 0, 1, 2, 3, 4] left
# [4, 5, 6, 0, 1, 2, 3] left
# [3, 4, 5, 6, 0, 1, 2] center
# [2, 3, 4, 5, 6, 0, 1] center
# [1, 2, 3, 4, 5, 6, 0] center

# [0, 1, 2, 5, 6]
# [6, 0, 1, 2, 5]
# [5, 6, 0, 1, 2]
# [2, 5, 6, 0, 1]
# [1, 2, 5, 6, 0]

DEBUG = True

class Solution:
    def search(self, nums: [int], target: int) -> int:
        # find pivot point
        left = 0
        right = len(nums) - 1
        pivot = 0

        while left < right:
            center = (left + right) // 2

            if DEBUG:
                print(left, center, right)

            if center >= 0 and nums[center] < nums[center - 1]:
                pivot = center
                break

            if nums[left] <= nums[center] <= nums[right]:
                pivot = left
                break
            elif nums[center] <= nums[right] <= nums[left]:
                right = center - 1
            elif nums[right] <= nums[left] <= nums[center]:
                left = center + 1
        else:
            pivot = left

        # find index
        left = pivot
        right = len(nums) + pivot - 1

        while left <= right:
            center = (left + right) // 2

            if center >= len(nums):
                adj_center = center - len(nums)
            else:
                adj_center = center

            center_num = nums[adj_center]

            if center_num == target:
                return adj_center
            elif center_num < target:
                left = center + 1
            else:
                right = center - 1

        return -1

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = []
        print(sol.search(input, 7))
