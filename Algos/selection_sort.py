nums = [13, 46, 24, 52, 20, 9]

# O(n^2)
def selection_sort(nums):
    for i in range(len(nums)):
        minPos = i
        for j in range(i+1, len(nums)):
            if(nums[j] < nums[minPos]):
                minPos = j
        # swapping
        temp = nums[i]
        nums[i] = nums[minPos]
        nums[minPos] = temp
    return 

selection_sort(nums)
print(nums)

