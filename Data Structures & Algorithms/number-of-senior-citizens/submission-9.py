class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = []
        
        for idx in range(len(details)):
            if details[idx][11 : 13] > "60":
                result.append(details[idx])
        return len(result)