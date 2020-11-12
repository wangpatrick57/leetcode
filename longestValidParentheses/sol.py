class Solution:
    def longestValidParentheses(self, s: str) -> int:
        start_paren_stack = []
        end_paren_sizes = dict()
        end_paren_starts = dict()

        for i, c in enumerate(s):
            if c == '(':
                start_paren_stack.append(i)
            elif c == ')':
                if len(start_paren_stack) == 0:
                    continue

                start_i = start_paren_stack.pop()

                # case where it's a simple ()
                if i - 1 == start_i:
                    end_paren_sizes[i] = 2
                    end_paren_starts[i] = start_i

                # case where one encloses another single group
                if (i - 1) in end_paren_starts and end_paren_starts[i - 1] == start_i + 1:
                    end_paren_sizes[i] = end_paren_sizes[i - 1] + 2
                    end_paren_starts[i] = start_i

                # case where two are touching (())() (not mutually exclusive)
                if start_i > 0 and (start_i - 1) in end_paren_starts:
                    end_paren_sizes[i] = end_paren_sizes[i] + end_paren_sizes[start_i - 1]
                    end_paren_starts[i] = end_paren_starts[start_i - 1]

        return max(end_paren_sizes.values()) if len(end_paren_sizes) > 0 else 0

sol = Solution()
print(sol.longestValidParentheses('(()'))
