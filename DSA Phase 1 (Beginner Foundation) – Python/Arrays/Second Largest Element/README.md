# Second Largest Element in an Array

## 📌 Problem Statement

Given an array of integers, find the **second largest distinct element**.

If no second largest element exists (all elements are the same), print **-1**.

---

## Example 1

### Input

```text
5
10 20 5 8 15
```

### Output

```text
15
```

### Explanation

Largest element = **20**

Second largest element = **15**

---

## Example 2

### Input

```text
6
5 5 4 3 2 1
```

### Output

```text
4
```

---

## Example 3

### Input

```text
4
10 10 10 10
```

### Output

```text
-1
```

### Explanation

All elements are the same, so there is no second distinct largest element.

---

# 💡 Approach

Traverse the array only once while maintaining two variables:

* **largest** → Stores the largest element found so far.
* **second_largest** → Stores the second largest distinct element.

Whenever a larger element is found:

* Move the current `largest` to `second_largest`.
* Update `largest`.

If the current element is:

* Smaller than `largest`
* Greater than `second_largest`
* Different from `largest`

Then update `second_largest`.

Finally, if `second_largest` is still negative infinity, print `-1`.

---

# 🧠 Algorithm

1. Read the array.
2. Initialize:

   * `largest = -∞`
   * `second_largest = -∞`
3. Traverse the array.
4. If the current element is greater than `largest`:

   * Assign `largest` to `second_largest`.
   * Update `largest`.
5. Otherwise, if the current element is:

   * Greater than `second_largest`
   * Not equal to `largest`
     then update `second_largest`.
6. If `second_largest` is still `-∞`, print `-1`.
7. Otherwise, print `second_largest`.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print(-1)
else:
    print(second_largest)
```

---

# ▶️ Dry Run

### Input

```text
10 20 5 8 15
```

| Current Number | Largest | Second Largest |
| -------------: | ------: | -------------: |
|             10 |      10 |             -∞ |
|             20 |      20 |             10 |
|              5 |      20 |             10 |
|              8 |      20 |             10 |
|             15 |      20 |             15 |

Output:

```text
15
```

---

# ⏱️ Complexity Analysis

## Time Complexity

The array is traversed only once.

```text
O(n)
```

---

## Space Complexity

Only two extra variables are used:

* `largest`
* `second_largest`

Therefore:

```text
O(1)
```

---

# 🎯 Key Concepts

* Array Traversal
* Conditional Statements
* Variable Tracking
* Distinct Elements
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### Duplicate Largest Elements

Input

```text
5
5 5 4 3 2
```

Output

```text
4
```

---

### All Elements Same

Input

```text
4
10 10 10 10
```

Output

```text
-1
```

---

### Negative Numbers

Input

```text
5
-10 -5 -20 -1 -7
```

Output

```text
-5
```

Using `float('-inf')` ensures the algorithm works correctly even when the array contains only negative numbers.

---

# 🧩 Pattern

**Pattern:** Array Traversal

This problem teaches how to maintain multiple values while traversing an array only once, without sorting.

---

# 📚 Related Problems

* Largest Element in an Array
* Third Largest Element
* Kth Largest Element
* Move Zeroes
* Find Maximum and Minimum
* Best Time to Buy and Sell Stock

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How to find the second largest element without sorting.
* Why using `float('-inf')` handles negative numbers correctly.
* How to update multiple tracking variables in a single traversal.
* How to achieve an optimal solution with **O(n)** time and **O(1)** space.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms
