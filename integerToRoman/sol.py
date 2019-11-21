DEBUG = True

class Solution:
    def intToRoman(self, num: int) -> str:
        rom_vals = dict()
        rom_vals[1] = 'I'
        rom_vals[4] = 'IV'
        rom_vals[5] = 'V'
        rom_vals[9] = 'IX'
        rom_vals[10] = 'X'
        rom_vals[40] = 'XL'
        rom_vals[50] = 'L'
        rom_vals[90] = 'XC'
        rom_vals[100] = 'C'
        rom_vals[400] = 'CD'
        rom_vals[500] = 'D'
        rom_vals[900] = 'CM'
        rom_vals[1000] = 'M'

        rom_str = ''
        rom_tot = 0

        for val in sorted(rom_vals.keys(), reverse = True):
            while num - rom_tot >= val:
                rom_str += rom_vals[val]
                rom_tot += val

        return rom_str

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()

        while True:
            str_input = input('enter an integer between 0 and 3999: ')

            if str_input == 'BREAK':
                break

            print('answer = %s' %(sol.intToRoman(int(str_input))))
