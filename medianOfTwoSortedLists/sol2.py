# create two lists called pars1 and pars2 which are 1 longer than nums1 and nums2
# have par1 start out at len(pars1) // 2 and pars2 at len(pars2) // 2
# length of pars1 and pars2 below
# 4 6 4+6=10 total_len=8 par_goal=4
# 5 7 5+7=12 total_len=10 par_goal=5
# 4 7 4+7=11 total_len=9 par_goal=4
#
# have par1 start at len(pars1) // 2
# have par2 start at par_goal - par1
# if left1 and right1 are both less than left2 and right 2, set min1 to par1 + 1
# if left1 and right1 are both greater than left2 and right 2, set max1 to par1 - 1
# if left1 >= left2 and right1 <= right2 or left1 <= left2 and right1 <= right2, you win!

MAX_INT = 'max'
MIN_INT = 'min'
DEBUG = False

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        total_len = len(nums1) + len(nums2)
        par_goal = total_len // 2

        if len(nums1) <= len(nums2):
            nums_s = nums1
            nums_b = nums2
        else:
            nums_s = nums2
            nums_b = nums1

        min_s = 0
        max_s = len(nums_s) + 1
        par_s = (min_s + max_s) // 2
        par_b = par_goal - par_s
        (left_s, right_s, left_b, right_b) = self._get_nums(par_s, par_b, nums_s, nums_b)

        while self._less_than(right_s, left_b) or self._less_than(right_b, left_s):
            if self._less_than(right_s, left_b):
                min_s = par_s + 1
            else:
                max_s = par_s - 1

            par_s = (min_s + max_s) // 2
            par_b = par_goal - par_s
            (left_s, right_s, left_b, right_b) = self._get_nums(par_s, par_b, nums_s, nums_b)

        if total_len % 2 == 0:
            if DEBUG:
                print(left_s, left_b, right_s, right_b, sep = ' ')

            return (self._max(left_s, left_b) + self._min(right_s, right_b)) / 2
        else:
            return self._max(self._max(left_s, left_b), self._min(right_s, right_b))

    def _get_nums(self, par1: int, par2: int, nums1: int, nums2: int) -> (int or str, int or str, int or str, int or str):
        if DEBUG:
            print(par1, par2, sep = ' ')

        if par1 != 0:
            left1 = nums1[par1 - 1]
        else:
            left1 = MIN_INT

        if par1 != len(nums1) + 1 - 1:
            right1 = nums1[par1]
        else:
            right1 = MAX_INT

        if par2 != 0:
            left2 = nums2[par2 - 1]
        else:
            left2 = MIN_INT

        if par2 != len(nums2) + 1 - 1:
            right2 = nums2[par2]
        else:
            right2 = MAX_INT

        return (left1, right1, left2, right2)

    def _less_than(self, num1: int or str, num2: int or str) -> bool:
        if type(num1) is str and type(num2) is str:
            if num1 == num2:
                return False
            elif num1 == MIN_INT:
                return True
        elif type(num1) is str:
            if num1 == MIN_INT:
                return True
            elif num1 == MAX_INT:
                return False
        elif type(num2) is str:
            if num2 == MIN_INT:
                return False
            elif num2 == MAX_INT:
                return True
        else:
            return num1 < num2

    def _max(self, num1: int or str, num2: int or str) -> int or str:
        if self._less_than(num1, num2):
            return num2
        else:
            return num1

    def _min(self, num1: int or str, num2: int or str) -> int or str:
        if self._less_than(num1, num2):
            return num1
        else:
            return num2

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        nums1 = [5,6,7,8]
        nums2 = [1,2,3,4]
        print('answer = ' + str(sol.findMedianSortedArrays(nums1, nums2)))
