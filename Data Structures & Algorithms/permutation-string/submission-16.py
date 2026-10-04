
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1Freq = [0] * 26
        windowFreq = [0] * 26

        if len(s1) > len(s2):
            return False
        
        for ch in s1:
            s1Freq[ord(ch.lower()) - ord('a')] += 1

        for idx in range(len(s1)):
            windowFreq[ord(s2[idx].lower()) - ord('a')] += 1

        if s1Freq == windowFreq:
            return True

        for r in range(len(s1), len(s2)):
            windowFreq[ord(s2[r].lower()) - ord('a')] += 1
            windowFreq[ord(s2[r - len(s1)].lower()) - ord('a')] -= 1

            if s1Freq == windowFreq:
                return True
        return False
        



        

