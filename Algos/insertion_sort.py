nums = [13, 46, 24, 52, 20, 9]

# O(n^2) - worst and average case
# O(n) - best case - when array is already sorted
def bubble_sort(nums):
    for i in range(1, len(nums)):
        while i > 0 and nums[i] < nums[i-1]:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            i -= 1
    return


bubble_sort(nums)
print(nums)