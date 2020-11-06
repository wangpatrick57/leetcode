class Solution:
    def groupAnagrams(self, words: [str]) -> [[str]]:
        processed_words = []
        groups = []

        for word in words:
            processed_words.append(self._process(word))

        for word in processed_words:
            found_group = False

            for group in groups:
                rep_group_word = group[0]

                if word['length'] == rep_group_word['length'] and self._processed_words_equal(word, rep_group_word):
                    group.append(word)
                    found_group = True
                    break

            if not found_group:
                groups.append([word])

        return [[processed_word['word'] for processed_word in group] for group in groups]

    def _process(self, word: str) -> {str: int}:
        processed = {'length': len(word), 'word': word}

        for letter in word:
            if letter not in processed:
                processed[letter] = 0

            processed[letter] += 1

        return processed

    def _processed_words_equal(self, a: {str: int}, b: {str: int}) -> bool:
        if a['length'] != b['length']:
            return False

        if len(a.keys()) != len(b.keys()):
            return False

        for key in a:
            if key != 'word':
                if not (key in a and key in b and a[key] == b[key]):
                    return False

        return True

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
