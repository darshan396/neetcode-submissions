class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        result = []
        for i in range(len(nums)):
            result.append(i)
            rem = target - nums[i]
            if rem in dic and dic[rem] != i:
                result.append(dic[rem])
                break
            result.pop()
        return result
        