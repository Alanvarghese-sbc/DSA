# Linear Search

## 📌 Problem Statement

Given an array of integers and a target element, find the **index** of the target element.

If the target element is not present in the array, print `-1`.

---

## Example 1

### Input

```text
5
10 20 30 40 50
30
```

### Output

```text
2
```

### Explanation

The target element `30` is found at index `2`.

---

## Example 2

### Input

```text
5
10 20 30 40 50
100
```

### Output

```text
-1
```

### Explanation

The target element is not present in the array.

---

# 💡 Approach

Linear Search works by checking each element one by one from the beginning of the array until the target element is found.

* Traverse the array from index `0` to `n-1`.
* Compare each element with the target.
* If a match is found:

  * Print its index.
  * Stop searching using `break`.
* If the loop completes without finding the target, print `-1`.

---

# 🧠 Algorithm

1. Read the size of the array.
2. Read the array elements.
3. Read the target element.
4. Initialize a boolean variable `is_found` as `False`.
5. Traverse the array.
6. If the current element equals the target:

   * Set `is_found = True`.
   * Print the index.
   * Exit the loop.
7. If `is_found` is still `False`, print `-1`.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

target = int(input())

is_found = False

for i in range(n):
    if arr[i] == target:
        is_found = True
        print(i)
        break

if not is_found:
    print(-1)
```

---

# ▶️ Dry Run

### Input

```text
5
10 20 30 40 50
40
```

| Iteration | Index | Element | Target | Found |
| --------- | ----: | ------: | -----: | :---: |
| 1         |     0 |      10 |     40 |   ❌   |
| 2         |     1 |      20 |     40 |   ❌   |
| 3         |     2 |      30 |     40 |   ❌   |
| 4         |     3 |      40 |     40 |   ✅   |

Output

```text
3
```

---

# ⏱️ Complexity Analysis

## Time Complexity

### Best Case

The target is found at the first position.

```text
O(1)
```

### Worst Case

The target is found at the last position or does not exist.

```text
O(n)
```

### Average Case

The target is found somewhere in the middle.

```text
O(n)
```

---

## Space Complexity

Only a few extra variables are used (`i`, `target`, `is_found`).

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Array Traversal
* Linear Search
* Boolean Flag
* Loop Control (`break`)
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### Element at First Position

Input

```text
5
10 20 30 40 50
10
```

Output

```text
0
```

---

### Element at Last Position

Input

```text
5
10 20 30 40 50
50
```

Output

```text
4
```

---

### Element Not Present

Input

```text
5
10 20 30 40 50
99
```

Output

```text
-1
```

---

### Single Element (Found)

Input

```text
1
100
100
```

Output

```text
0
```

---

### Single Element (Not Found)

Input

```text
1
100
50
```

Output

```text
-1
```

---

# 🧩 Pattern

**Pattern:** Array Traversal

Linear Search checks each element sequentially until the target is found or the array ends.

---

# 📚 Related Problems

* Binary Search
* First Occurrence of an Element
* Last Occurrence of an Element
* Search Insert Position
* Find Minimum and Maximum Element

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How Linear Search works.
* How to traverse an array using a loop.
* How to stop a loop using `break`.
* How to use a boolean flag to track whether an element is found.
* Why Linear Search has **O(n)** time complexity in the average and worst cases.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms
