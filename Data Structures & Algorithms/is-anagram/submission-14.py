# Since the two strings have to have the same characters to be
# anagrams, picking each unique character from one string and 
# discarding it after seeing it the second time must result to 0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26

        if len(s) != len(t):
            return False

        for ch in s:
            freq[ord(ch.lower()) - ord('a')] += 1

        for cht in t:
            freq[ord(cht.lower()) - ord('a')] -= 1

        for idx in range(len(freq)):
            if freq[idx] != 0:
                return False
        return True
        

        