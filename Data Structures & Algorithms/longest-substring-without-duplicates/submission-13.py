class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in freq:
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            freq[s[r]] += 1
            result = max(result, r - l + 1)
        return result




        