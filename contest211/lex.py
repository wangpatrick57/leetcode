# if b is odd we can apply a to all digits, otherwise only to odd ones
# first apply a to all applicable digits, then rotate with b

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s_len = len(s)
        all_a = self.find_all_possible_transforms(a, 10)
        all_b = self.find_all_possible_transforms(b, s_len)
        min = '9' * s_len

        for test_a_even in ([0] if b % 2 == 0 else all_a):
            for test_b in all_b:
                for test_a_odd in all_a:
                    test_string = self.build_string(s, s_len, test_a_even, test_a_odd, test_b)

                    if test_string < min:
                        min = test_string
                        print(test_a_odd, test_b, test_string)

        return min

    def build_string(self, base_s: str, base_len: int, a_even: int, a_odd: int, b: int) -> str:
        new_string = ''

        for i in range(base_len):
            new_string += self.string_add(base_s[(i - b) % base_len], a_even if i % 2 == 0 else a_odd)

        return new_string

    def string_add(self, s: str, a: int) -> str:
        return chr(((ord(s[0]) - 48 + a) % 10) + 48)

    def find_all_possible_transforms(self, n: int, base: int) -> [int]:
        found_transforms = []
        curr_transform = 0

        for _ in range(base):
            if curr_transform in found_transforms:
                break

            found_transforms.append(curr_transform)
            curr_transform = (curr_transform + n) % base

        return found_transforms

sol = Solution()
print(sol.findLexSmallestString('43987654', 7, 3))
