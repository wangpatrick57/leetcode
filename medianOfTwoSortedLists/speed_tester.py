import sol
import random
from datetime import datetime

def _gen_list(length: int, max: int) -> [int]:
    ret = [0] * length

    for i in range(length):
        ret[i] = random.randint(0, max)

    return ret

if __name__ == '__main__':
    sol = sol.Solution()
    interval = 10
    min = interval
    max = 10000

    for total_len in range(min, max, interval):
        # n = random.randint(0, total_len)
        n = total_len // 2
        m = total_len - n
        nums1 = _gen_list(n, max)
        nums2 = _gen_list(m, max)
        nums1.sort()
        nums2.sort()
        start_time = datetime.now()
        trash = sol.findMedianSortedArrays(nums1, nums2)
        end_time = datetime.now()
        print(f'%d,%d' %(total_len, (end_time - start_time).microseconds))
