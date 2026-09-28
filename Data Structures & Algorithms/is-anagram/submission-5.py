class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch.lower()) - ord('a')] += 1

        for ch in t:
            frequency[ord(ch.lower()) - ord('a')] -= 1

        for i in range(len(frequency)):
            if frequency[i] != 0:
                return False
        
        return True
        