from collections import deque

DEBUG = True

class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        answer = []
        word_len = len(words[0])
        word_required_count = dict()

        for i, word in enumerate(words):
            if word not in word_required_count:
                word_required_count[word] = 0

            word_required_count[word] += 1

        for start_i in range(word_len):
            # check all alignments
            num_words_included = 0
            curr_word_queue = deque()
            word_included_count = dict()

            for i, word in enumerate(words):
                if word not in word_included_count:
                    word_included_count[word] = 0

            for i in range(start_i, len(s), word_len):
                # add word to queue
                word_to_add = s[i : i + word_len]
                curr_word_queue.append(word_to_add)

                if word_to_add in word_included_count:
                    word_included_count[word_to_add] += 1

                    if word_included_count[word_to_add] <= word_required_count[word_to_add]:
                        num_words_included += 1

                # after checking enough words, start removing a word every time
                if len(curr_word_queue) > len(words):
                    popped_word = curr_word_queue.popleft()

                    if popped_word in word_included_count:
                        if DEBUG:
                            assert word_included_count[popped_word] != 0, 'word_included_count is zero for popped_word'

                        word_included_count[popped_word] -= 1

                        if word_included_count[popped_word] < word_required_count[popped_word]:
                            num_words_included -= 1

                # add to answer if necessary
                if num_words_included == len(words):
                    answer.append(i - word_len * (num_words_included - 1))

                if DEBUG:
                    print(f'nwi: {num_words_included}, cwq: {curr_word_queue}')
                    assert num_words_included <= len(words), 'num_words_included exceeded len(words)'

        return answer

if DEBUG:
    sol = Solution()
    print(sol.findSubstring('aaaaaaaaaaa', ['aa', 'aa']))
