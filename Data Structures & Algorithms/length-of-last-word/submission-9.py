class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == ' ' and length == 0:
                continue

            elif s[idx] == ' ':
                return length

            length += 1
        return length