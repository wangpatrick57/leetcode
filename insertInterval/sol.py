class Solution:
    def insert(self, intervals, new_interval):
        ans = []
        i = 0

        # add all lesser non-overlapping intervals
        while i < len(intervals):
            interval = intervals[i]

            if interval[1] < new_interval[0]:
                ans.append(interval)
                i += 1
            else:
                break

        # add new interval with all overlapping ones
        combined_interval = new_interval

        while i < len(intervals):
            interval = intervals[i]

            if not (interval[1] < new_interval[0] or new_interval[1] < interval[0]):
                combined_interval[0] = min(interval[0], new_interval[0])
                combined_interval[1] = max(interval[1], new_interval[1])
                i += 1
            else:
                break

        ans.append(combined_interval)

        # add all greater non-overlapping intervals
        while i < len(intervals):
            interval = intervals[i]

            if new_interval[1] < interval[0]:
                ans.append(interval)
                i += 1

        return ans

if __name__ == '__main__':
    s = Solution()

    # empty
    assert s.insert([], [2, 3]) == [[2, 3]]

    # just before
    assert s.insert([[0, 1]], [2, 3]) == [[0, 1], [2, 3]]

    # just after
    assert s.insert([[5, 6]], [2, 3]) == [[2, 3], [5, 6]]

    # no overlap
    assert s.insert([[0, 1], [5, 6]], [2, 3]) == [[0, 1], [2, 3], [5, 6]]

    # edge overlap
    assert s.insert([[0, 2], [5, 6]], [2, 3]) == [[0, 3], [5, 6]]

    # lesser overlap
    assert s.insert([[0, 3], [5, 6]], [2, 4]) == [[0, 4], [5, 6]]

    # greater overlap
    assert s.insert([[0, 1], [5, 9]], [2, 6]) == [[0, 1], [2, 9]]

    # double overlap
    assert s.insert([[0, 3], [8, 16]], [2, 9]) == [[0, 16]]

    # lesser capture overlap
    assert s.insert([[0, 4], [9, 16]], [1, 2]) == [[0, 4], [9, 16]]

    # greater capture overlap
    assert s.insert([[0, 4], [9, 16]], [11, 12]) == [[0, 4], [9, 16]]

    # new total capture overlap
    assert s.insert([[0, 1], [2, 3], [4, 5], [6, 7]], [0, 8]) == [[0, 8]]
