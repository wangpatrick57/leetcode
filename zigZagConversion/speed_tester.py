from random import choice
from string import ascii_uppercase
from datetime import datetime
import sol

def main():
    string = _gen_rand_str(10000)

    start_rows = 0
    end_rows = 10000
    interval = 100
    solution = sol.Solution()

    for num_rows in range(start_rows, end_rows, interval):
        start_time = datetime.now()
        trash = solution.convert(string, num_rows)
        end_time = datetime.now()
        print(f'%d,%d' %(num_rows, (end_time - start_time).microseconds))

def _gen_rand_str(length: int) -> str:
    return ''.join(choice(ascii_uppercase) for i in range(length))

if __name__ == '__main__':
    main()
