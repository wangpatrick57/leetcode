class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)

        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]
