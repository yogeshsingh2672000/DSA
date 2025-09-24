nums = [13, 46, 24, 52, 20, 9]

# O(n^2) - worst and average case
def bubble_sort(nums):
    for i in range(len(nums), -1, -1):
        for j in range(i-1):
            if(nums[j] > nums[j+1]):
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return 

# best case - when array is already sorted O(n)
def bubble_sort(nums):
    for i in range(len(nums), -1, -1):
        swapped = False
        for j in range(i-1):
            if(nums[j] > nums[j+1]):
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                swapped = True
        if swapped:
            break
    return 

bubble_sort(nums)
print(nums)

