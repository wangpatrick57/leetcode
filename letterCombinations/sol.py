DEBUG = True

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0:
            return list()

        num_to_char = self._create_num_to_char()
        combinations = list()
        num_combinations = 1

        for digit in digits:
            num_combinations *= len(num_to_char[digit])

        for i in range(num_combinations):
            combinations.append('')

        curr_period = num_combinations

        for i in range(len(digits)):
            digit = digits[i]
            curr_period //= len(num_to_char[digit])
            curr_char_index = 0

            for j in range(num_combinations):
                combinations[j] += num_to_char[digit][curr_char_index % len(num_to_char[digit])]

                if j % curr_period == curr_period - 1:
                    curr_char_index += 1

        return combinations

    def _create_num_to_char(self) -> dict:
        start = 97
        num_chars = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        ends = list()
        num_to_char = dict()
        sum = 0

        for num in num_chars:
            sum += num
            ends.append(sum)

        for i in range(2, 10):
            key = str(i)
            chars = list()

            for j in range(num_chars[i]):
                chars.append(chr(start + ends[i - 1] + j))

            num_to_char[key] = chars

        return num_to_char

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = ''
        print(sol.letterCombinations(input))
