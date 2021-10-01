class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        last_num = None
        next_free_index = 0
        num_curr_num = 0

        for i in range(len(nums)):
            num = nums[i]

            if num == last_num:
                num_curr_num += 1
            else:
                num_curr_num = 0

            if num_curr_num == 0 or num_curr_num == 1:
                nums[next_free_index] = num
                next_free_index += 1
                last_num = num

        return next_free_index

if __name__ == '__main__':
    l = [1, 1, 1, 2, 2, 3]
    s = Solution()
    print(s.removeDuplicates(l), '5')
    print(l, '[1, 1, 2, 2, 3, _]')
    l = [1]
    print(s.removeDuplicates(l), '1')
    print(l, '[1]')
    l = [1, 2, 5, 8, 8, 10]
    print(s.removeDuplicates(l), '6')
    print(l, '[1, 2, 5, 8, 8, 10]')
    l = [0, 0, 1, 1, 1, 1, 2, 2, 3]
    print(s.removeDuplicates(l), '7')
    print(l, '[0, 0, 1, 1, 2, 2, 3, _, _]')
    l = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3]
    print(s.removeDuplicates(l), '7')
    print(l, '[0, 0, 1, 1, 2, 2, 3, _, _, _]')
    l = [0, 0, 0, 1, 2, 2, 3]
    print(s.removeDuplicates(l), '6')
    print(l, '[0, 0, 1, 2, 2, 3, _]')
