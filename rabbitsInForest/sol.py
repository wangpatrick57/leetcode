class Solution:
    def numRabbits(self, answers: [int]) -> int:
        existing_dict = dict()
        min_rabbits = 0

        for answer in answers:
            if answer not in existing_dict:
                existing_dict[answer] = 0

            if existing_dict[answer] == 0:
                min_rabbits += answer + 1

            existing_dict[answer] += 1

            # can't use mod cuz answer can be 0
            if existing_dict[answer] > answer:
                existing_dict[answer] = 0

        return min_rabbits

if __name__ == '__main__':
    s = Solution()
    print(s.numRabbits([0, 0, 0]), '3')
    print(s.numRabbits([0, 0, 1, 1, 1]), '6')
    print(s.numRabbits([1, 1, 2]), '5')
    print(s.numRabbits([10, 10, 10]), '11')
    print(s.numRabbits([2, 2, 2]), '3')
    print(s.numRabbits([2, 2, 2, 2]), '6')
