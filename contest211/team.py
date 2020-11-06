from collections import defaultdict

class Solution:
    def bestTeamScore(self, scores: [int], ages: [int]) -> int:
        score_ref = dict()

        for i, age in enumerate(ages):
            if age not in score_ref:
                score_ref[age] = []

            score_ref[age].append(scores[i])

        for scores in score_ref.values():
            scores.sort()

        ages = list(set(ages))
        ages.sort(reverse = True)

        print('score_ref', score_ref)

        current_scores = defaultdict(int)

        for age in ages:
            new_scores = dict()
            prev_score = score_ref[age][0]
            score_count = 1

            for i in range(1, len(score_ref[age]) + 1):
                if i == len(score_ref[age]):
                    score = None
                else:
                    score = score_ref[age][i]

                if prev_score != score:
                    points_loss = 0

                    print()
                    print('current_scores', str(current_scores).split('>, ')[1][:-1])

                    for s, n in current_scores.items():
                        if s < prev_score:
                            points_loss += s * n

                    print('points_loss', points_loss)
                    print('prev_score', prev_score, 'score_count', score_count)
                    print()

                    if points_loss < prev_score * score_count:
                        self.prune(current_scores, prev_score)
                        new_scores[prev_score] = score_count

                    score_count = 1
                else:
                    score_count += 1

                prev_score = score

            # apply changes
            for score, count in new_scores.items():
                current_scores[score] += count

        print(current_scores)

        total = 0

        for s, n in current_scores.items():
            total += s * n

        return total

    def prune(self, d, score: int) -> None:
        for s in d:
            if d[s] > 0 and s < score:
                d[s] -= 1

sol = Solution()
print('answer', sol.bestTeamScore([6,5,1,7,6,5,5,4,10,4], [3,2,5,3,2,1,4,4,5,1]))
