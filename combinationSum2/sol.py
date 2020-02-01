from copy import copy

DEBUG = True

class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        def helper(addends: [int], candidates: {int: int}, target: int) -> [[int]]:
            addends_list = list()
            checked_candidates = set()
            last_candidate = None

            for i in range(len(candidates)):
                candidate = candidates[i]

                if i >= 1 and candidate == candidates[i - 1]:
                    continue

                test_addends = copy(addends)
                test_addends.append(candidate)

                if candidate == target:
                    addends_list.append(test_addends)
                elif candidate < target:
                    addends_list.extend(helper(test_addends, candidates[(i + 1):], target - candidate))
                else:
                    break

            return addends_list

        return helper(list(), sorted(candidates), target)

if DEBUG:
    if __name__ == '__main__':
        s = Solution()
        candidates = [0]
        target = 1
        print(s.combinationSum2(candidates, target))
