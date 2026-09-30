class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency = defaultdict(int)
        r = len(s1) - 1

        for idx in range((len(s2) - len(s1)) + 1):
            frequency["".join(sorted(s2[idx : r + 1]))] += 1
            r += 1

        return frequency["".join(sorted(s1))] != 0

