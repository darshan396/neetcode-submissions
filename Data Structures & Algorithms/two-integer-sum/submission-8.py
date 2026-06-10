class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        sub = {}
        for i in range(len(nums)):
            sub[nums[i]] = i

        for j in range(len(nums)):
            rem = target - nums[j]
            ans.append(j)
            if rem in sub and sub[rem] != j:
                ans.append(sub[rem])
                break
            ans.pop(0)

        return ans