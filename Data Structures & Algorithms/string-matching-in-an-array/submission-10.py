class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
       return [w for w in words if any(w != o and w in o for o in words)]
            


        