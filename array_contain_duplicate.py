def check(nums):
    unique_Set = set(nums)
    return len(unique_Set) < len(nums)

var = [1,2,3,2,1,3,4,5]
print(check(var))