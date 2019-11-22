DEBUG = True

class Solution:
    def max_area(self, heights: [int]) -> int:
        largest_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            left_height = heights[left]
            right_height = heights[right]

            area = min(left_height, right_height) * abs(left - right)

            if area > largest_area:
                largest_area = area

            if left_height <= right_height:
                left += 1

            if right_height <= left_height:
                right -= 1

        return largest_area

    def brute_max_area(self, heights: [int]) -> int:
        largest_area = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                area = min(heights[i], heights[j]) * abs(i - j)

                if area > largest_area:
                    largest_area = area

        return largest_area

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()
        input = [2, 1, 5, 4, 3, 1, 2, 0]
        print('answer = ' + str(sol.max_area(input)))
