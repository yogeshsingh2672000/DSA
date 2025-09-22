n = 5
name = 'yogesh'

# Recusrion
def printName(name, n):
    if n < 0:
        return
    print(name)
    printName(name, n-1)

n = 10
# Recursion: printing from n to 1
def decrement(n):
    if n == 0:
        return
    print(n)
    decrement(n-1)

n = 2
# Backtracking: printing from 1 to n
def increment(n):
    if n == 0:
        return
    increment(n-1)
    print(n)

# Calculate sum of first n natural numbers using recursion
def sumOfN(n):
    if(n==0):
        return 0
    return n + sumOfN(n-1)

# Calculate factorial of n using recursion
def factorialOfN(n):
    if(n==0):
        return 1
    return n * sumOfN(n-1)

arr = [1, 2, 3, 4, 5, 6]
# Reverse an array using recursion
def reverseArray(arr, start, end):
    if(start >= end):
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start+1, end-1)

str = "false"
# Check if a string is palindrome using recursion
def checkPalindrome(str, start, end):
    if(start >= end):
        return True
    if(str[start] != str[end]):
        return False
    return checkPalindrome(str, start+1, end-1)

# Calculate nth Fibonacci number using recursion
def febonacci(n):
	if(n == 0):
		return 0
	if(n == 1):
		return 1
	return febonacci(n-1) + febonacci(n-2)

# Print all contigious substrings of an array using recursion with count
arr = [3, 1, 2]
n = len(arr)
tempArr = []
count = 0
def contigiousSubString(i, tempArr):
    global count # we can do it without global also by returning count
    if(i >= n):
          print(tempArr)
          count = count + 1
          return
    tempArr.append(arr[i])
    contigiousSubString(i+1, tempArr)
    tempArr.pop()  
    contigiousSubString(i+1, tempArr)
    return


nums = [2,5,6,9] 
target = 9
n = len(nums)
i = 0
sum = 0
result = []

# Function to find combinations without repetition allowed
def subsetSum(i, arr, sum, target, n, result):
    if(i == n):
        if(sum == target):
            result.append(arr.copy()) # we need to append a copy of arr because arr is mutable and will change in further calls *refernce*
        return
    
    # case pick
    arr.append(nums[i])
    sum += nums[i]
    subsetSum(i+1, arr, sum, target, n, result)

    # case do not pick
    arr.pop()
    sum -= nums[i]
    subsetSum(i+1, arr, sum, target, n, result)


# Function to find combinations with repetition allowed
def subsetSumWithRepetition(i, arr, sum, target, n, result):
    if(sum == target):
        result.append(arr.copy())
        return
    if(sum > target or i >= n):
        return
    
    # case pick (we stay at same index i since we can reuse)
    arr.append(nums[i])
    subsetSumWithRepetition(i, arr, sum + nums[i], target, n, result)
    
    # case do not pick (move to next index)
    arr.pop()
    subsetSumWithRepetition(i+1, arr, sum, target, n, result)

# Test the new function
# result_with_repetition = []
# subsetSumWithRepetition(0, [], 0, target, n, result_with_repetition)
# print("Combinations with repetition allowed:", result_with_repetition)


def find_menu_path(menu, target_label):
    for item in menu:
        # If the current item matches, return it as a path
        if item["label"] == target_label:
            return [item["label"]]
        
        # Otherwise, search in children
        if item.get("children"):
            sub_path = find_menu_path(item["children"], target_label)
            if sub_path:  # found in children
                return [item["label"]] + sub_path
    
    # Not found at this level
    return None


# Example usage
menu = [
    {"label": "Home", "children": []},
    {
        "label": "About",
        "children": [
            {"label": "Team", "children": []},
            {"label": "Company", "children": []}
        ]
    }
]

# print(find_menu_path(menu, "Company"))  # ["About", "Company"]
# print(find_menu_path(menu, "Blog"))     # None

nums = [1]

def firstMissingPositive(nums):
    nums.sort()
    print("newNums", nums)
    maxNum = nums[-1]

    if(maxNum <= 0):
        return 1

    print("maxNum", maxNum)

    for i in range(1, 2*maxNum):
        print("i", i)
        if (i not in nums):
            return i
        continue
    return maxNum + 1
        
# print(firstMissingPositive(nums))


nums = [1,2,0]
def firstMissingPositive(nums):
    n = len(nums)
    
    # Place each number in its correct position if possible
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # swap nums[i] with nums[nums[i]-1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Now, the first index where nums[i] != i+1 gives the missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all 1...n are present, then answer is n+1
    return n + 1

# print(firstMissingPositive(nums))
n = 200
mem = [-1] * (n+1)
def feb(n):
    if(n == 0 or n == 1):
        return n
    if(mem[n] != -1):
        return mem[n]
    mem[n] = feb(n-1) + feb(n-2)
    return mem[n]
print(feb(n))

