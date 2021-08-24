class Solution(object):
    def trap(self, height):
        left_i = -1
        left_max = 0
        right_i = len(height)
        right_max = 0
        water = 0

        while right_i - left_i > 1:
            if left_max <= right_max:
                left_i += 1
                left_max = max(left_max, height[left_i])
                change = min(left_max, right_max) - height[left_i]

                if change > 0:
                    water += change
            elif left_max > right_max:
                right_i -= 1
                right_max = max(right_max, height[right_i])
                change = min(left_max, right_max) - height[right_i]

                if change > 0:
                    water += change

            print(f'li: {left_i}, ri: {right_i}, change: {change}')

        return water

# [0, 1, 0, 3, 3, 2, 0, 1]
# [0, 1, 0, 3, 0, 3, 1, 2]

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([0, 1, 0, 3, 3, 2, 0, 1]))
    print(s.trap([0, 1, 0, 3, 0, 3, 1, 2]))
