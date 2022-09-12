class Solution:
    def merge(self, intervals):
        intervals.sort()
        out = []
        build_start = None
        build_end = None

        for s, e in intervals:
            if build_start == None:
                build_start = s
                build_end = e

            if s <= build_end:
                build_end = max(e, build_end)
            else:
                out.append([build_start, build_end])
                build_start = s
                build_end = e

        if build_start != None:
            out.append([build_start, build_end])
            build_start = None
            build_end = None

        return out

if __name__ == '__main__':
    s = Solution()
    # arr = [[4, 5], [1, 3], [2, 4], [6, 7]]
    arr = []
    arr = [[1, 3], [1, 2], [1, 1], [1, 3], [3, 5], [5, 5], [7, 7]]
    out = s.merge(arr)
    print(out)
