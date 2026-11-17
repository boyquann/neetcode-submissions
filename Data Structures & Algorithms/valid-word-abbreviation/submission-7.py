class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)

        if len(abbr) > len(word):
            return False

        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < n and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1
                i += num
            else:
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
        return i == m and j == n




        