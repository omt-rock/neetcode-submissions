from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums)
        d = {}
        l1 = []

        for i in s:
            c = nums.count(i)
            d[i] = c

        sorted_dict = dict(sorted(d.items(), key=itemgetter(1), reverse=True))
        l = list(sorted_dict.keys())
        for j in range(k):
            l1.append(l[j])
        
        return l1
