class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        num_set = set()
        for val in nums:
            if val in num_set:
                return True
            else:
                num_set.add(val)
        return False
        
#      if len of array == 1 return false 
# iterate through array and add each value to set before adding check if that value is already present inside the set. If it is present then we have duplicate and return true else false
        
        