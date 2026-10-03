class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        s1Freq = [0] * 26
        s2Freq = [0] * 26

        if len(s1) > len(s2):
            return False

        for ch in s1:
            s1Freq[ord(ch.lower()) - ord("a")] +=1

        for idx in range(len(s1)):
            s2Freq[ord(s2[idx].lower()) - ord('a')] += 1

        if s1Freq == s2Freq:
            return True

        for r in range(len(s1), len(s2)):
            s2Freq[ord(s2[r].lower()) - ord('a')] += 1
            s2Freq[ord(s2[r - len(s1)].lower()) - ord('a')] -= 1

            if s1Freq == s2Freq:
                return True
        return False
                
        


        



        

