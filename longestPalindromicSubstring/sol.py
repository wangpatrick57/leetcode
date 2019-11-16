#  0 1 2 3
# 012345678
# input 0, output -1 and 0
# input 1, output -1 and 1
# input 2, output 0 and 1
# input 3, output 0 and 2
# input 4, output 1 and 2

DEBUG = True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_tot = len(s) * 2 + 1
        longest_len = 0
        longest_str = ''

        for pal_ind in range(pal_tot):
            left_ind = pal_ind // 2 - 1
            right_ind = (pal_ind + 1) // 2

            while left_ind >= 0 and right_ind < len(s):
                if s[left_ind] == s[right_ind]:
                    left_ind -= 1
                    right_ind += 1
                else:
                    break

            pal_start = left_ind + 1
            pal_end = right_ind - 1 + 1
            this_len = pal_end - pal_start

            if this_len > longest_len:
                longest_len = this_len
                longest_str = s[pal_start: pal_end]

        return longest_str

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()

        while True:
            input_str = input('enter an input: ')

            if input_str == 'break':
                break

            print('answer = ' + str(sol.longestPalindrome(input_str)))
