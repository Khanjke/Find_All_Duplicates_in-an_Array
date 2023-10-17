class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        data = {}
        for i in range(len(nums)):
            result.append(nums[i]) if nums[i] in data else data.update({nums[i]: 1})
        return result


#nums = [1]
#print(findDuplicates(nums))