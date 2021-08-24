PRESENT = 0
NOT_PRESENT = -1

# [0, 4, -1, 3, 2] start
# [-1, 4, -1, 3, 2] first pass
# [-1, 4, -1, 3, 2] second pass

# big loop
# [-1, 4, 5, 3, 5]
# [-1, -1, 0, 0, 5] saved = 3, new_saved = 5

# loop ending on -1
# [-1, 4, 5, 3, -1]

class Solution(object):
    def firstMissingPositive(self, nums):
        print('start:', nums)

        # first pass, destroy all numbers we don't care about
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] - 1 >= len(nums):
                nums[i] = NOT_PRESENT

        print('first pass:', nums)

        # second pass, fill out array with PRESENT and NOT_PRESENT
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue

            val = nums[i]
            nums[i] = NOT_PRESENT
            saved = nums[val - 1]
            nums[val - 1] = PRESENT

            while saved > 0:
                new_saved = nums[saved - 1]
                nums[saved - 1] = PRESENT

                if new_saved == saved:
                    break

                saved = new_saved

        print('second pass:', nums)

        # third pass, return answer
        for i in range(len(nums)):
            if nums[i] == NOT_PRESENT:
                return i + 1

        return len(nums) + 1

    def test(self, nums):
        i = 0

        while i < len(nums):
            j = nums[i] - 1

            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

if __name__ == '__main__':
    s = Solution()
    nums = [2]
    ans = s.test(nums)
    print('ans:', ans)
