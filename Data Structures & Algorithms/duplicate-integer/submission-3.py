# Since a set is an unordered collection of unique elements,
# that attribute mean sets do not have duplicates.
# Therefore, the length of the set of the array should equal 
# the length of the array if there are no duplicates, otherwise 
# it is not equal

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))