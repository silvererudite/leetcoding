class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        set2 = set()
        set2.add(len(nums))
        for i in range(1, len(nums)):
            set2.add(i)
        return set2.difference(set1)
    ### OR ##

    def findDisappearedNumbers(self, nums):
        result = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
