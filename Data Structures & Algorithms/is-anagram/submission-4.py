class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_1 = []
        set_2 = []

        for i in s:
            set_1.append(i)
        for j in t:
            set_2.append(j)
        
        if sorted(set_1) == sorted(set_2):
            return True
        else:
            return False
