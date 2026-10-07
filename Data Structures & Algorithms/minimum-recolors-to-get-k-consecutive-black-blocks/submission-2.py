# We want to perform the minimum number of operations such that we get a window of size k containing consecutive B blocks
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = defaultdict(int)
        L = 0
        result = float('inf')

        for R in range(len(blocks)):
            freq[blocks[R]] += 1

            while (R - L + 1) == k:
                result = min(result, (R - L + 1) - freq['B'])
                freq[blocks[L]] -= 1
                L += 1
        return result
            



            
        