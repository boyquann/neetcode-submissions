class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for idx in range(1, len(strs)):
                if len(strs[idx]) == i or strs[0][i] != strs[idx][i]:
                    return result
            result += strs[0][i]
        return result