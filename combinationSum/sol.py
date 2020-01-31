from copy import copy

DEBUG = True

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        if target < 0:
            return [[]]

        def helper(candidates: [int], target: int) -> [[int]]:
            if target == 0:
                return [[]]
            elif target < 0:
                return None

            addends_list = []

            for i in range(len(candidates)):
                candidate = candidates[i]

                lower_addends_list = helper(candidates[i:], target - candidate)

                if DEBUG:
                    print('a', target - candidate, lower_addends_list)

                if lower_addends_list == None:
                    continue

                for lower_addends in lower_addends_list:
                    lower_addends.append(candidate)
                    addends_list.append(lower_addends)

            return addends_list

        return helper(sorted(candidates), target)

if DEBUG:
    if __name__ == '__main__':
        candidates = [0]
        target = 8
        s = Solution()

        print('answer = ', s.combinationSum(candidates, target))
