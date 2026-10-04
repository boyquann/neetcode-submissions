
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = [0] * 26
        windowFreq = [0] * 26

        if len(s1) > len(s2):
            return False
        
        for ch in s1:
            s1Freq[ord(ch) - ord('a')] += 1

        for idx in range(len(s1)):
            windowFreq[ord(s2[idx]) - ord('a')] += 1

        if s1Freq == windowFreq:
            return True

        for r in range(len(s1), len(s2)):
            windowFreq[ord(s2[r]) - ord('a')] += 1
            windowFreq[ord(s2[r - len(s1)]) - ord('a')] -= 1

            if s1Freq == windowFreq:
                return True
        return False
        



        

