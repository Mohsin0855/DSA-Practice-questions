def getmin(arr):
    mini_value = float('inf')
    for var in arr:
        if var < mini_value:
         mini_value = var
    return mini_value

def getmax(arr):
    max_value = float('-inf')
    for num in arr:
        if num > max_value:
           max_value = num
    return max_value


var = [4,5,6,2,3,1,8,9]
print('maximum value is:',getmax(var))

print('minimum vlue is:',getmin(var))