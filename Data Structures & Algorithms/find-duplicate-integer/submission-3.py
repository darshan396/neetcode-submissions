class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = []
        ans = 0
        for i in range(len(nums)):
            if nums[i] in temp:
                ans = nums[i]
                break
            else:
                temp.append(nums[i])
        return ans