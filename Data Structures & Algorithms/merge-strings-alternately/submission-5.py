class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        n, m = len(word1), len(word2)
        output = ""

        while i < len(word1) and j < len(word2):
            output += word1[i]
            i += 1
            output += word2[j]
            j += 1
        output += word1[i : ] + word2[j :]
        return output



        