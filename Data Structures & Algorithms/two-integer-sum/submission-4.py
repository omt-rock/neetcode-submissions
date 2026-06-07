class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        d = {}

        for index, num in enumerate(nums):
            d[num] = index

        for i in range(len(nums)):
            if (target - nums[i]) in nums and i != d[target - nums[i]]:
                l.append(i)
                l.append(d[target - nums[i]])
                break
        return l
        
        
        
