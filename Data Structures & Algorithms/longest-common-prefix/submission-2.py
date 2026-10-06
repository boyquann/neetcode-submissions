["bathroom", "bat","bag","bank","band"]
# We need to go through each character in the string and compare
# since a prefix has to be the shortest word in a sentence, it doesn't matter how many times we iterate, we just need to make sure to end early
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
        

