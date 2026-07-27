# First Non-Repeating Element

## 📌 Problem Statement

Given an array of integers, find the **first element that appears only once**.

If no such element exists, print **-1**.

---

## Example 1

### Input

```text
7
4 5 1 2 0 4 1
```

### Output

```text
5
```

### Explanation

Frequency of each element:

```
4 → 2
5 → 1
1 → 2
2 → 1
0 → 1
```

The first element whose frequency is `1` is **5**.

---

## Example 2

### Input

```text
5
1 1 2 2 3
```

### Output

```text
3
```

---

## Example 3

### Input

```text
4
7 7 8 8
```

### Output

```text
-1
```

---

# 💡 Approach

The solution is completed in **two passes**.

### Step 1: Count Frequency

Use a dictionary to count how many times each element appears.

Example:

```python
{
    4: 2,
    5: 1,
    1: 2,
    2: 1,
    0: 1
}
```

---

### Step 2: Find the First Non-Repeating Element

Traverse the original array again.

The first element whose frequency is `1` is the answer.

If no such element exists, print `-1`.

---

# 🧠 Algorithm

1. Read the array.
2. Create an empty dictionary.
3. Count the frequency of every element.
4. Traverse the original array.
5. If an element has frequency `1`, print it and stop.
6. If no element is found, print `-1`.

---

# 💻 Python Code

```python
n = int(input())
arr = list(map(int, input().split()))

freq = {}

# Count frequency
for num in arr:
    freq[num] = freq.get(num, 0) + 1

found = False

# Find first non-repeating element
for num in arr:
    if freq[num] == 1:
        print(num)
        found = True
        break

if not found:
    print(-1)
```

---

# ⏱️ Complexity Analysis

### Time Complexity

* Frequency counting → **O(n)**
* Finding the first non-repeating element → **O(n)**

**Overall:** `O(n)`

---

### Space Complexity

The dictionary stores the frequency of each unique element.

**Space:** `O(n)`

---

# 🎯 Key Concepts

* Dictionary (`dict`)
* Hashing
* Frequency Counting
* Two-Pass Algorithm
* Array Traversal
* Time Complexity Analysis

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How to use a dictionary for frequency counting.
* Why traversing the original array preserves the correct order.
* How to solve lookup problems efficiently using hashing.
* How to analyze time and space complexity.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms
