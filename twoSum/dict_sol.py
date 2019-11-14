class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = dict()

        for i in range(len(nums)):
            comp_num = target - nums[i]

            if comp_num in index_dict:
                return [index_dict[comp_num], i]
            else:
                index_dict[nums[i]] = i
