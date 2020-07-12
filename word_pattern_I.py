class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        char_map = {}
        str_map = {}
        str_arr = str.split(' ')

        if len(pattern) != len(str_arr):
            return False

        for char, str_ in zip(pattern, str_arr):
            if (char in char_map and char_map[char] != str_) or (str_ in str_map and str_map[str_] != char):
                return False
            char_map[char] = str_
            str_map[str_] = char

        return True
