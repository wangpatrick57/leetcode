import math
import time

DEBUG = True

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0

        curr_sum = divisor
        sums = list()

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            og_quotient_inc = 1
        else:
            og_quotient_inc = -1

        quotient = og_quotient_inc
        found_quotient = False

        while True:
            # increment up
            quotient_inc = og_quotient_inc
            index = 0

            while abs(curr_sum) <= abs(dividend):
                if abs(curr_sum) == abs(dividend) or (abs(curr_sum) < abs(dividend) and abs(curr_sum + divisor) > abs(dividend)):
                    found_quotient = True
                    break

                if index >= len(sums):
                    sums.append(curr_sum)

                curr_sum += sums[index]
                quotient += quotient_inc
                quotient_inc += quotient_inc

                if DEBUG:
                    print(curr_sum, quotient, quotient_inc, sums[index])

                index += 1

            if found_quotient:
                break

            # increment down
            quotient_inc = og_quotient_inc
            index = 0

            while abs(curr_sum) > abs(dividend):
                curr_sum -= sums[index]
                quotient -= quotient_inc
                quotient_inc += quotient_inc

                if DEBUG:
                    print(curr_sum, quotient, quotient_inc, sums[index])

                index += 1

        if quotient < -pow(2, 31):
            quotient = -pow(2, 31)

        if quotient > pow(2, 31) - 1:
            quotient = pow(2, 31) - 1

        return quotient

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        print('answer = ' + str(sol.divide(1, 2)))
