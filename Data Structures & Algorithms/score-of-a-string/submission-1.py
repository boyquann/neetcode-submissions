class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        codes = []

        for ch in s:
            codes.append(ord(ch))

            if len(codes) > 1:
                for i in codes:
                    score += abs(codes[0] - codes[1])
                    codes.pop(0)
        return score