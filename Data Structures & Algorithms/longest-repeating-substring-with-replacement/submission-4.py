# Find longest subarry that allows at most k replacements
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        result = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
            
