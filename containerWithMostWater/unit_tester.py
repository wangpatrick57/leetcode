import random
import sol

def _gen_input(length: int) -> [int]:
    ret = [0] * length

    for i in range(length):
        ret[i] = random.randint(0, length)

    return ret

if __name__ == '__main__':
    solution = sol.Solution()

    for i in range(10000):
        input_length = random.randint(2, 10)
        input = _gen_input(input_length)
        fast_area = solution.max_area(input)
        brute_area = solution.brute_max_area(input)

        if fast_area != brute_area:
            print(f'fast_area = %d but brute_area = %d for the input %s' %(fast_area, brute_area, input))
