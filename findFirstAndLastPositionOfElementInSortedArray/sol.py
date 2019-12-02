DEBUG = True

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1, -1]

        first = -1
        last = -1

        # find first
        left = 0
        right = len(nums)

        while left <= right:
            center = (left + right) // 2 # center is a splitter
            (left_to_target, right_to_target) = self._find_to_targets(nums, target, center)

            # doing stuff based on left and right to targets
            if left_to_target == -1 and right_to_target == 0:
                first = center
                break
            elif left_to_target == -1 and right_to_target == -1:
                left = center + 1
            else:
                right = center - 1

        # find last
        left = 0
        right = len(nums)

        while left <= right:
            center = (left + right) // 2 # center is a splitter
            (left_to_target, right_to_target) = self._find_to_targets(nums, target, center)

            # doing stuff based on left and right to targets
            if left_to_target == 0 and right_to_target == 1:
                last = center - 1
                break
            elif left_to_target == 1 and right_to_target == 1:
                right = center - 1
            else:
                left = center + 1

        return [first, last]

    def _compare(self, a: int, b: int) -> int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def _find_to_targets(self, nums: [int], target: int, center: int) -> (int, int):
        if center == 0:
            left_to_target = -1 # -1 means less than, 0 means equals, 1 means greater than
            right_to_target = self._compare(nums[center], target)
        elif center == len(nums):
            left_to_target = self._compare(nums[center - 1], target)
            right_to_target = 1
        else:
            left_to_target = self._compare(nums[center - 1], target)
            right_to_target = self._compare(nums[center], target)

        return (left_to_target, right_to_target)

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = [1, 1, 2]
        print('answer = ' + str(sol.searchRange(input, 2)))
