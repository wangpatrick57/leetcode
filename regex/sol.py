# how to handle n*nnn? if there's a n* followed by any number of n's, combine them into "at least (some number of) n's"
# how to handle n*.?
# how to handle one .*? match from the end
# how to handle multiple .*'s? match from the end for the last one

# turn n* into nnn
# make sure all the *'s transformed end up the same length as s
# backtracking: for all valid lengths of the first *, search lengths of next stars

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # preprocess
        num_stars = 0

        for i in range(len(p)):
            c = p[i]

            if c == '*':
                num_stars += 1
            else:
                if num_stars > 0 and num_stars % 2 == 0:
                    return False
                elif num_stars > 1 and num_stars % 2 == 1:
                    p = p[:i - num_stars] + '*' + p[i:]

                num_stars = 0

        static_chunks = p.split('*')
        num_stars = len(static_chunks) - 1
        wildcards = []

        for i in range(len(static_chunks) - 1):
            chunk = static_chunks[i]

            if len(chunk) == 0:
                return False

            wildcards.append(chunk[-1])
            static_chunks[i] = chunk[:-1]

        # check if length is valid
        min_exp_length = len(p) - 2 * num_stars

        if min_exp_length > len(s) or (len(static_chunks) == 1 and min_exp_length != len(s)):
            return False

        return self._is_match_helper(s, static_chunks, 0, 0, len(s) - min_exp_length, wildcards)

    def _is_match_helper(self, s: str, static_chunks: [str], s_start: int, chunk_index: int, length_left: int, wildcards: [str]) -> bool:
        # base case: no wildcards left
        if chunk_index == len(wildcards):
            return self._expansion_is_valid(s[s_start:], static_chunks[chunk_index])
        else:
            curr_chunk = static_chunks[chunk_index]

            for curr_wild_length in range(length_left + 1):
                s_end = s_start + len(curr_chunk) + curr_wild_length
                mini_s = s[s_start:s_end]
                mini_e = curr_chunk + (wildcards[chunk_index] * curr_wild_length)

                if self._expansion_is_valid(mini_s, mini_e):
                    print(wildcards[chunk_index], curr_wild_length)

                    if self._is_match_helper(s, static_chunks, s_end, chunk_index + 1, length_left - curr_wild_length, wildcards):
                        return True

            return False

    # s and e must be the same length
    def _expansion_is_valid(self, s: str, e: str) -> bool: # e has only ., not *
        if len(s) != len(e):
            return False

        for cs, ce in zip(s, e):
            if ce != '.' and cs != ce:
                return False

        return True

sol = Solution()
print(sol.isMatch('aab', 'a*****b'))
