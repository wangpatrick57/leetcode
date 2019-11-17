# first line
# if numRows == 2
# A C E G
# B D F
#
# if numRows == 3
# A   E   I
# B D F H
# C   G
# 4 interval
#
# if numRows == 4
# A     G     M
# B   F H   L N
# C E   I K   O Q
# D     J     P
# 6 interval
# cols = 0 from 0 to 4
# cols = 1 from 5 to 10
# cols = 2 from 11 to 16
#
# if numRows == 5
# A       I
# B     H
# C   G
# D F
# E
# 8 interval

DEBUG = False

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        interval = 2 * (num_rows - 1)
        cols = (len(s) + interval - num_rows) // interval

        if DEBUG:
            print('cols = ' + str(cols))
            
        row_num = 0
        ret = ''

        # first line
        for row_num in range(num_rows):
            if row_num >= 0 and row_num < len(s):
                ret += s[row_num]

            if DEBUG:
                print('row_num = ' + str(row_num))

            for i in range(cols):
                slant = -row_num + interval * (i + 1)
                vert = row_num + interval * (i + 1)

                if row_num != 0 and row_num != num_rows - 1:
                    if slant >= 0 and slant < len(s):
                        ret += s[slant]

                if vert >= 0 and vert < len(s):
                    ret += s[vert]

                if DEBUG:
                    print('slant = ' + str(slant))
                    print('vert = ' + str(vert))

        return ret

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        s = 'abcdefg'
        num_rows = 2
        print('answer = ' + sol.convert(s, num_rows))
