class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        set2 = set()
        set2.add(len(nums))
        for i in range(1, len(nums)):
            set2.add(i)
        return set2.difference(set1)
