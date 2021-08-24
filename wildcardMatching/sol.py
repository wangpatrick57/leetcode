class Solution(object):
    def isMatch(self, s, p):
        self._s = s
        self._p = p
        self._memo = dict()
        return self._helper(0, 0)

    def _helper(self, si, pi):
        tuple_key = (si, pi)

        if tuple_key in self._memo:
            return self._memo[tuple_key]

        if si > len(self._s) - 1 and pi > len(self._p) - 1:
            self._memo[tuple_key] = True
        elif pi > len(self._p) - 1:
            self._memo[tuple_key] = False
        else:
            if self._p[pi] == '?':
                if si > len(self._s) - 1:
                    self._memo[tuple_key] = False
                else:
                    self._memo[tuple_key] = self._helper(si + 1, pi + 1)
            elif self._p[pi] == '*':
                if si > len(self._s) - 1:
                    si_move = False
                else:
                    si_move = self._helper(si + 1, pi)

                if si_move:
                    self._memo[tuple_key] = True
                else:
                    pi_move = self._helper(si, pi + 1)
                    self._memo[tuple_key] = pi_move
            else:
                if si > len(self._s) - 1:
                    self._memo[tuple_key] = False
                elif self._s[si] != self._p[pi]:
                    self._memo[tuple_key] = False
                else:
                    self._memo[tuple_key] = self._helper(si + 1, pi + 1)

        return self._memo[tuple_key]

if __name__ == '__main__':
    s = Solution()
    assert s.isMatch('', '')
    assert s.isMatch('', '*')
    assert s.isMatch('a', 'a')
    assert not s.isMatch('a', 'aa')
    assert s.isMatch('a', 'a*')
    assert s.isMatch('a', '*')
    assert s.isMatch('a', '**')
    assert s.isMatch('abcdef', '*')
    assert s.isMatch('abcdef', '*f')
    assert not s.isMatch('abcdef', '*d')
    assert s.isMatch('abcdef', '*d*')
    assert s.isMatch('abcdef', '*?d*')
    assert not s.isMatch('abcdef', 'abc?def')
    assert s.isMatch('abcdef', 'abc?ef')
    print(s.isMatch('abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab', '*aabb***aa**a******aa*'))
    print(s.isMatch('babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab', '***bba**a*bbba**aab**b'))
