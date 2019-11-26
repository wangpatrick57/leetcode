DEBUG = True

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        num = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            prev_num = num
            curr_index = len(nums) - 1 - i
            num = nums[curr_index]

            if prev_num > num:
                # find next largest
                next_largest_index = curr_index + 1

                for j in range(next_largest_index + 1, len(nums)):
                    if nums[j] > num and nums[j] < nums[next_largest_index]:
                        next_largest_index = j

                nums[curr_index] = nums[next_largest_index]
                nums[next_largest_index] = num
                self.quick_sort(nums, curr_index + 1, len(nums) - 1)
                return

        nums.sort()

    def quick_sort(self, list: [int], start: int, end: int) -> None:
        if start < end:
            partition_index = self.partition(list, start, end)
            self.quick_sort(list, start, partition_index - 1)
            self.quick_sort(list, partition_index + 1, end)

    def partition(self, list: [int], start: int, end: int) -> int:
        partition = list[start]
        left = start + 1
        right = end

        while left <= right:
            while left <= right and list[left] <= partition:
                left += 1

            while left <= right and list[right] >= partition:
                right -= 1

            if left > right:
                list[start] = list[right]
                list[right] = partition
                return right
            else:
                temp = list[left]
                list[left] = list[right]
                list[right] = temp

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = [3,2,1]
        print(input)
        sol.nextPermutation(input)
        print(input)
