class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_dict = dict()
        start_index = 0
        longest_len = 0

        for i in range(len(s)):
            c = s[i]

            if c in index_dict.keys():
                if i - start_index > longest_len:
                    longest_len = i - start_index

                last_rep_index = index_dict[c]

                for j in range(start_index, last_rep_index + 1):
                    del index_dict[s[j]]

                start_index = last_rep_index + 1

            index_dict[c] = i

        if len(s) - start_index > longest_len:
            longest_len = len(s) - start_index

        return longest_len
