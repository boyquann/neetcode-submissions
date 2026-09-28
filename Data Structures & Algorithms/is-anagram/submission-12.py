class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch.lower()) - ord('a')] += 1

        for ch in t:
            frequency[ord(ch.lower()) - ord('a')] -= 1

        for idx in frequency:
            if idx != 0:
                return False

        return True
   