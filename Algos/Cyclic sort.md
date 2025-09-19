# 🔄 Cyclic Sort & Its Role in First Missing Positive Problem

## What is Cyclic Sort?

Cyclic Sort is a **linear-time in-place sorting algorithm** used when:

- You have `n` numbers.
- All numbers lie in the range `[1, n]` (no gaps, no duplicates ideally).

👉 **Key Idea**  
Put each number directly in its correct index (`num → index = num - 1`).  
Keep swapping until every number is in its right place.

---

## 📝 Algorithm Steps

1. Start at index `i = 0`.
2. If `nums[i]` is not at its correct index (`nums[i] != i+1`) → swap it with the element at its correct index.
   - Example: `nums[i] = 3` → should go to index `2`.
3. Else → move `i` forward.
4. Repeat until the end of the array.

---

## 🔧 Example Walkthrough

Let’s sort `[3, 5, 2, 1, 4]` using Cyclic Sort.

**Initial**  
[3, 5, 2, 1, 4]

- `i=0`, `nums[0] = 3` → correct index of `3` is `2`.  
  Swap → `[2, 5, 3, 1, 4]`

- Still `i=0`, `nums[0] = 2` → correct index of `2` is `1`.  
  Swap → `[5, 2, 3, 1, 4]`

- Still `i=0`, `nums[0] = 5` → correct index of `5` is `4`.  
  Swap → `[4, 2, 3, 1, 5]`

- Still `i=0`, `nums[0] = 4` → correct index of `4` is `3`.  
  Swap → `[1, 2, 3, 4, 5]`

Now everything is in place ✅

**Final Sorted**  
[1, 2, 3, 4, 5]

---

## ⏱️ Complexity

- **Time:** `O(n)` (each number is swapped at most once).
- **Space:** `O(1)` (in-place, no extra array).

---

## 🌟 Why is Cyclic Sort Useful?

Works best when numbers are in `[1, n]`. Instead of fully sorting, you can use the idea for **index mapping problems**, like:

- Finding missing number(s).
- Detecting duplicates.
- **First Missing Positive (this problem).**

👉 In our problem, we don’t fully sort.  
We just use Cyclic Sort logic to put numbers in the right spots, then scan to find the missing positive.

---

# 🔗 How Cyclic Sort Fits into "First Missing Positive"

## ✅ Problem Recap

We want the **smallest missing positive integer** from an unsorted array.

Constraints:

- `O(n)` time
- `O(1)` extra space

---

## 🔗 How Cyclic Sort Helps

- Cyclic Sort’s idea = put each number `x` into index `x-1` if it’s valid (`1 ≤ x ≤ n`).
- Why?
  - The answer is always in `[1, n+1]`.
  - Worst case: If array has all numbers `1…n`, then missing number = `n+1`.
- So after rearrangement:
  - At index `i`, we should find `i+1`.
  - If not, then `i+1` is the missing positive.

---

## 🔄 Example: `nums = [3,4,-1,1]`

### Step 1: Rearrange (Cyclic Sort logic)

- `nums[0] = 3` → should be at index `2`.  
  Swap → `[ -1, 4, 3, 1 ]`

- `nums[0] = -1` → invalid, ignore.

- `nums[1] = 4` → should be at index `3`.  
  Swap → `[ -1, 1, 3, 4 ]`

- `nums[1] = 1` → should be at index `0`.  
  Swap → `[ 1, -1, 3, 4 ]`

- `nums[2] = 3` already in place.
- `nums[3] = 4` already in place.

✅ Rearranged: `[1, -1, 3, 4]`

---

### Step 2: Find the first missing positive

Scan from left:

- Index `0`: value `1` ✅
- Index `1`: expected `2`, but found `-1` ❌

👉 Answer = **2**

---

## 🎯 Why Cyclic Sort is Key

- Rearranges numbers into their correct spots in `O(n)`.
- After that, one linear scan gives the missing positive.
- Without it, we’d need:
  - Sorting → `O(n log n)`
  - Hash set → `O(n)` space

👉 Cyclic Sort logic = **Step 1 (placement)** in the optimized solution.  
👉 Linear scan = **Step 2 (detect missing)**.
