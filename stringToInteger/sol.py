DEBUG = True

class Solution:
    def myAtoi(self, s: str) -> int:
        mult_found = False
        phrase_started = False
        num_started = False
        tot = 0
        mult = 1
        int_min = -1 * pow(2, 31)
        int_max = pow(2, 31) - 1

        for c in s:
            if not c.isspace():
                phrase_started = True

                if c == '+' or c == '-':
                    if num_started:
                        break
                    elif mult_found:
                        return 0
                    else:
                        if c == '+':
                            mult = 1
                        elif c == '-':
                            mult = -1

                        mult_found = True
                elif c.isdigit():
                    tot = 10 * tot + int(c)
                    num_started = True
                else:
                    break
            else:
                if phrase_started:
                    break

        tot *= mult

        if tot < int_min:
            tot = int_min
        elif tot > int_max:
            tot = int_max

        return tot

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()

        while True:
            input_str = input()

            if input_str == 'BREAK':
                break
            else:
                print('answer = ' + str(sol.myAtoi(input_str)))
