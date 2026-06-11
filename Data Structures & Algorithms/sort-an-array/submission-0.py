class Solution:

    def merge(self ,left_sub_array: List[int], right_sub_array: List[int]) -> List[int]:
        n1 = len(left_sub_array)
        n2 = len(right_sub_array)

        i = 0
        j = 0
        sorted_array = []
        while i<n1 and j <n2:
            if left_sub_array[i] <= right_sub_array[j]:
                sorted_array.append(left_sub_array[i])
                i+=1
            else:
                sorted_array.append(right_sub_array[j])
                j+=1
            
        while i<n1:
            sorted_array.append(left_sub_array[i])
            i+=1
        
        while j<n2:
            sorted_array.append(right_sub_array[j])
            j+=1

        return sorted_array

    def sortArray(self, nums: List[int ]) -> List[int]:
        if len(nums) == 1:
            return nums
        left = 0
        right = len(nums) -1
        mid = (left+right) // 2

        left_sub_array = self.sortArray(nums[left:mid+1])
        right_sub_array = self.sortArray(nums[mid+1:right+1])

        return self.merge(left_sub_array,right_sub_array)