class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        s = len(set(nums))
        if l > s:
            return True
        else:
            return False
          