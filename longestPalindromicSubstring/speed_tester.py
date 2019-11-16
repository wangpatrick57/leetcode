from random import choice
from string import ascii_uppercase
from datetime import datetime
import sol

def main():
    start_len = 0
    end_len = 10000
    interval = 100
    solution = sol.Solution()

    for length in range(start_len, end_len, interval):
        string = _gen_rand_str(length)
        start_time = datetime.now()
        trash = solution.longestPalindrome(string)
        end_time = datetime.now()
        print(f'%d,%d' %(length, (end_time - start_time).microseconds))

def _gen_rand_str(length: int) -> str:
    return ''.join(choice(ascii_uppercase) for i in range(length))

if __name__ == '__main__':
    main()
