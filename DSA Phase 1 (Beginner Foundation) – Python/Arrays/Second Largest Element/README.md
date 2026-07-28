# 🥈 Second Largest Element in an Array (Without Using Built-in Functions)

## 📌 Problem Statement

Given an array of integers, find the **second largest distinct element** in the array.

**Do not use:**

- ❌ `sort()`
- ❌ `sorted()`
- ❌ `max()`

If there is **no second distinct largest element**, print `-1`.

---

## 📥 Input Format

- First line: An integer `n` (size of the array)
- Second line: `n` space-separated integers

---

## 📤 Output Format

Print the second largest distinct element.

If it doesn't exist, print `-1`.

---

## 🧾 Examples

### Example 1

#### Input

```text
5
10 20 5 8 15
```

#### Output

```text
15
```

---

### Example 2

#### Input

```text
6
5 5 4 3 2 1
```

#### Output

```text
4
```

---

### Example 3

#### Input

```text
4
10 10 10 10
```

#### Output

```text
-1
```

---

## 🧠 Approach

Instead of sorting the array, we traverse it **only once** while maintaining two variables:

- `largest`
- `second_largest`

Initially, both are assigned:

```python
float('-inf')
```

During traversal:

- If the current element is greater than `largest`
  - Move `largest` to `second_largest`
  - Update `largest`
- Otherwise, if it is:
  - Smaller than `largest`
  - Greater than `second_largest`
  - Not equal to `largest`
  
  Then update `second_largest`.

Finally, if `second_largest` is still `-inf`, it means no second largest element exists.

---

## 🔄 Algorithm

1. Read the array.
2. Initialize:
   - `largest = -∞`
   - `second_largest = -∞`
3. Traverse every element.
4. Update `largest` and `second_largest` accordingly.
5. If `second_largest` is unchanged, print `-1`.
6. Otherwise, print `second_largest`.

---

## 💻 Python Code

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

## 🧪 Dry Run

### Input

```text
5
10 20 5 8 15
```

### Initial Values

```text
largest = -∞
second_largest = -∞
```

| Current Number | Largest | Second Largest |
|---------------:|--------:|---------------:|
| 10 | 10 | -∞ |
| 20 | 20 | 10 |
| 5 | 20 | 10 |
| 8 | 20 | 10 |
| 15 | 20 | 15 |

### Output

```text
15
```

---

## 🧪 Dry Run (Duplicate Largest)

### Input

```text
6
5 5 4 3 2 1
```

| Current Number | Largest | Second Largest |
|---------------:|--------:|---------------:|
| 5 | 5 | -∞ |
| 5 | 5 | -∞ |
| 4 | 5 | 4 |
| 3 | 5 | 4 |
| 2 | 5 | 4 |
| 1 | 5 | 4 |

### Output

```text
4
```

---

## 🧪 Dry Run (All Elements Same)

### Input

```text
4
10 10 10 10
```

| Current Number | Largest | Second Largest |
|---------------:|--------:|---------------:|
| 10 | 10 | -∞ |
| 10 | 10 | -∞ |
| 10 | 10 | -∞ |
| 10 | 10 | -∞ |

Since `second_largest` was never updated,

### Output

```text
-1
```

---

## 💡 Why Use `float('-inf')`?

We initialize both variables to negative infinity.

```python
largest = float('-inf')
second_largest = float('-inf')
```

Why?

Because every integer is greater than negative infinity.

Example:

```python
10 > float('-inf')
```

Output:

```text
True
```

This allows the algorithm to work correctly even when the array contains negative numbers.

Example:

```text
-5 -2 -8 -1
```

Output:

```text
-2
```

---

## ⏱ Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

### Why?

- The array is traversed only once.
- Only two extra variables are used:
  - `largest`
  - `second_largest`

---

## 🔥 Key Concepts

- Array Traversal
- Linear Search
- Variable Tracking
- One-Pass Algorithm
- Constant Space
- Interview Optimization

---

## ⚠️ Edge Cases

### Single Element

**Input**

```text
1
5
```

**Output**

```text
-1
```

---

### All Elements Same

**Input**

```text
4
7 7 7 7
```

**Output**

```text
-1
```

---

### Duplicate Largest

**Input**

```text
5
10 20 20 15 5
```

**Output**

```text
15
```

---

### Negative Numbers

**Input**

```text
5
-5 -1 -8 -3 -2
```

**Output**

```text
-2
```

---

## 🎯 Pattern Learned

This problem teaches the **Array Traversal** pattern.

Instead of sorting the entire array, we keep track of only the two largest values while traversing once.

This makes the solution both efficient and interview-friendly.

---

## 🚀 Related Problems

- Largest Element in an Array
- Second Smallest Element
- Third Largest Element
- Best Time to Buy and Sell Stock
- Maximum Difference Between Two Elements
- Leaders in an Array

---

## 📚 What You Learned

✅ One-pass traversal

✅ Tracking multiple values simultaneously

✅ Handling duplicate values

✅ Using `float('-inf')`

✅ Solving without built-in functions

---

## 📌 Author

**Alan Varghese**
```