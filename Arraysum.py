def twoSum(nums, target):
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if (nums[j]+nums[i]) == target:
                    return [i, j]
        return []  
nums = [2,3,4,5,6,7,8,9] 
target = 13          
print(twoSum(nums, target))