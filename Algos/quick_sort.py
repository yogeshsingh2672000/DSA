nums = [13, 46, 24, 52, 20, 9]

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    return

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high


    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        
        while nums[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            swap(nums, i, j)

    swap(nums, low, j)
    return j


def quick_sort(nums, low, high):
    if(low < high):
        partition_index = partition(nums, low, high)
        quick_sort(nums, low, partition_index - 1)
        quick_sort(nums, partition_index + 1, high)
    pass


quick_sort(nums, 0, len(nums) - 1)
print(nums)

