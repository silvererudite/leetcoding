class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        elem_hash = [0] * 10**5
        for i in nums:
            elem_hash[i] += 1
        for i in elem_hash:
            if i == 1:
                return elem_hash.index(i)
