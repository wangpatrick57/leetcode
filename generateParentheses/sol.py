# **|| ((()))
# *|*| (()())
# |*|* ()()()
# ||** ())(()
# |**| ()
# *||* ()

DEBUG = True

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        ans = list()
        self._gen_parens(ans, '', 0, 0, n)
        return ans

    def _gen_parens(self, ans: [str], curr_str: str, curr_open: int, curr_close: int, n: int):
        if len(curr_str) == n * 2:
            if n == 0:
                return
            
            ans.append(curr_str)
            return

        if curr_open < n:
            self._gen_parens(ans, curr_str + '(', curr_open + 1, curr_close, n)

        if curr_close < n and curr_close < curr_open:
            self._gen_parens(ans, curr_str + ')', curr_open, curr_close + 1, n)

if DEBUG:
    if __name__ == '__main__':
        sol = Solution()

        while True:
            print(sol.generateParenthesis(int(input('enter an integer: '))))
