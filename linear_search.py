def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Target {target} found at index {i}")
            return i, target
    print(f"Target {target} not found")
    return -1, target


var = [2,3,1,4,54,6,8]
result = 54
print(linearSearch(var,result))

