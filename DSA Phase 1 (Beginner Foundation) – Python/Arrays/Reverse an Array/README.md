# 🔄 Reverse Array Using Two Pointers (Python)

## 📌 Problem Statement

Given an array of `n` integers, reverse the array **without using built-in functions** such as:

- ❌ `reverse()`
- ❌ `reversed()`
- ❌ Slicing (`[::-1]`)

Use the **Two Pointers** technique to reverse the array **in-place**.

---

## 📥 Input Format

- First line: An integer `n` (size of the array)
- Second line: `n` space-separated integers

---

## 📤 Output Format

Print the reversed array.

---

## 🧾 Example

### Input

```text
5
1 2 3 4 5
```

### Output

```text
5 4 3 2 1
```

---

## 🧠 Approach

Instead of creating a new array, we reverse the array **in-place** using two pointers.

- `left` starts at the beginning of the array.
- `right` starts at the end of the array.
- Swap the elements at both pointers.
- Move:
  - `left` one step forward.
  - `right` one step backward.
- Continue until both pointers meet or cross each other.

---

## 🔄 Algorithm

1. Read the array.
2. Initialize:
   - `left = 0`
   - `right = n - 1`
3. While `left <= right`:
   - Swap `arr[left]` and `arr[right]`
   - Increment `left`
   - Decrement `right`
4. Print the reversed array.

---

## 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

left = 0
right = n - 1

while left <= right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    left += 1
    right -= 1

print(*arr)
```

---

## 🧪 Dry Run

### Input

```text
5
1 2 3 4 5
```

### Initial Array

```text
1 2 3 4 5
↑       ↑
L       R
```

### After First Swap

```text
5 2 3 4 1
  ↑   ↑
  L   R
```

### After Second Swap

```text
5 4 3 2 1
    ↑
   L,R
```

Pointers meet, so the loop ends.

---

## 💡 Why Does Swapping Work?

Each swap places:

- The left element in its correct position from the end.
- The right element in its correct position from the beginning.

Since both pointers move toward the center, every element is moved exactly once.

---

## ⏱ Time & Space Complexity

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

### Explanation

- The loop performs approximately `n/2` swaps.
- In Big-O notation, constants are ignored:

```text
O(n/2)
↓

O(n)
```

Only three extra variables are used:

- `left`
- `right`
- `temp`

Therefore, the space complexity is **O(1)**.

---

## 🔥 Key Concepts

- Arrays
- Two Pointers
- Swapping
- In-place Algorithm
- Constant Space Complexity

---

## ⚠️ Edge Cases

### Single Element

**Input**

```text
1
10
```

**Output**

```text
10
```

---

### Even Number of Elements

**Input**

```text
4
1 2 3 4
```

**Output**

```text
4 3 2 1
```

---

### Odd Number of Elements

**Input**

```text
5
1 2 3 4 5
```

**Output**

```text
5 4 3 2 1
```

---

## 📚 Pattern Learned

This problem introduces the **Two Pointers** pattern.

The same technique is used in many interview questions, such as:

- Reverse String
- Valid Palindrome
- Move Zeroes
- Remove Duplicates from Sorted Array
- Container With Most Water
- Squares of a Sorted Array
- Rotate Array

Learning this pattern makes many array and string problems much easier.

---

## 🚀 Related Problems

- Reverse String
- Rotate Array
- Reverse Part of an Array
- Valid Palindrome
- Move Zeroes

---

## 📌 Author

**Alan Varghese**