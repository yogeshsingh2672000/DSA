nums = [13, 46, 24, 52, 20, 9]

# O(n log n) time | O(n) space
def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if(nums[left] <= nums[right]):
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    
    # Copy remaining elements from left half
    while left <= mid:
        temp.append(nums[left])
        left += 1

    # Copy remaining elements from right half
    while right <= high:
        temp.append(nums[right])
        right += 1

    # Copy back to original array
    for i in range(low, high + 1):
        nums[i] = temp[i - low]

def merge_sort(nums, low, high):
    if(low==high):
        return
    mid = (low + high) // 2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid + 1, high)
    merge(nums, low, mid, high)

    return


merge_sort(nums, 0, len(nums) - 1)
print(nums)

