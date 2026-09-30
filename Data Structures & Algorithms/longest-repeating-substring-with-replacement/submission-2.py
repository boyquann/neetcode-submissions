class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        frequency = defaultdict(int)

        for r in range(len(s)):
            frequency[s[r]] += 1
            maxFreq = max(frequency.values())

            if (r - l + 1) - maxFreq > k:
                frequency[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        
        return result