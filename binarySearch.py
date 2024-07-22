def binarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start +(end - start) // 2
        if arr[mid] == target:
            print(f"value {target} found at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"value {target} is greater than {arr[mid]}, searching right half")
            start = mid + 1
        else:
            print(f"value {target} is less than {arr[mid]}, searching left half")
            end = mid - 1
    print(f"value {target} not found")
    return -1

var = [1,2,3,4,5,6,7,8]
target  = 1
print(binarySearch(var,target))

