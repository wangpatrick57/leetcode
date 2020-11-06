class Solution:
    def bestTeamScore(self, scores: [int], ages: [int]) -> int:
        # double sort
        combined = [(age, score) for age, score in zip(ages, scores)]
        combined.sort()
        print(combined)
        memo = dict()
        return self.best_team_score_for_curr_min(len(combined) - 1, None, combined, memo)

    def best_team_score_for_curr_min(self, index: int, last_included_index: int, combined: [(int, int)], memo: {(int, int): int}) -> int:
        if (index, last_included_index) in memo:
            return memo[(index, last_included_index)]
        else:
            test_age = combined[index][0]
            test_score = combined[index][1]

            if last_included_index == None:
                last_included_age = float('inf')
                last_included_score = float('inf')
            else:
                last_included_age = combined[last_included_index][0]
                last_included_score = combined[last_included_index][1]

            if index == 0:
                if test_age == last_included_age or test_score <= last_included_score:
                    best_score = combined[index][1]
                else:
                    best_score = 0
            else:
                score_if_excluded = self.best_team_score_for_curr_min(index - 1, last_included_index, combined, memo)

                if test_age == last_included_age or test_score <= last_included_score:
                    score_if_included = test_score + self.best_team_score_for_curr_min(index - 1, index, combined, memo)
                    best_score = max(score_if_included, score_if_excluded)
                else:
                    best_score = score_if_excluded

            memo[(index, last_included_index)] = best_score
            return best_score


sol = Solution()
# print('answer', sol.bestTeamScore([6,5,1,7,6,5,5,4,10,4], [3,2,5,3,2,1,4,4,5,1]))
print('answer2', sol.bestTeamScore([9,2,8,8,2], [4,1,3,3,5]))
