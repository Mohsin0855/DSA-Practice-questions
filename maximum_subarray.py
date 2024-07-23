def max_subArray(nums):
     max_current = max_global = nums[0]
     for num in nums[1:]:
         max_current = max(num, max_current + num)
         if max_current > max_global:
             max_global = max_current
     return max_global

var = [2,3,5,-4,-6,2,5,6]
print(max_subArray(var))





















