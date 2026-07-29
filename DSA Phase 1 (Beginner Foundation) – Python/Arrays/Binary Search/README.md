# Binary Search

## 📌 Problem Statement

Given a **sorted array** of integers and a target element, find the **index** of the target element.

If the target element is not present in the array, print `-1`.

> **Note:** Binary Search works only on **sorted arrays**.

---

# Example 1

### Input

```text
7
10 20 30 40 50 60 70
50
```

### Output

```text
4
```

### Explanation

The target element `50` is present at index `4`.

---

# Example 2

### Input

```text
7
10 20 30 40 50 60 70
35
```

### Output

```text
-1
```

### Explanation

The target element is not present in the array.

---

# 💡 Approach

Instead of checking every element one by one, Binary Search repeatedly divides the search space into two halves.

* Find the middle element.
* If the middle element is the target, print its index.
* If the target is smaller than the middle element, continue searching in the left half.
* If the target is greater than the middle element, continue searching in the right half.
* Repeat until the element is found or the search space becomes empty.

---

# 🧠 Algorithm

1. Read the size of the array.
2. Read the sorted array.
3. Read the target element.
4. Initialize:

   * `left = 0`
   * `right = n - 1`
5. While `left <= right`:

   * Find the middle index:

     ```python
     mid = (left + right) // 2
     ```
   * If `arr[mid] == target`, print `mid` and stop.
   * If `arr[mid] > target`, search the left half.
   * Otherwise, search the right half.
6. If the loop ends without finding the target, print `-1`.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

target = int(input())

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[mid] > target:
        right = mid - 1

    else:
        left = mid + 1

else:
    print(-1)
```

---

# ▶️ Dry Run

### Input

```text
7
10 20 30 40 50 60 70
60
```

| Iteration | Left | Right | Mid | Middle Value | Action            |
| --------- | ---: | ----: | --: | -----------: | ----------------- |
| 1         |    0 |     6 |   3 |           40 | Search Right Half |
| 2         |    4 |     6 |   5 |           60 | Target Found      |

Output

```text
5
```

---

# ⏱️ Complexity Analysis

## Time Complexity

### Best Case

The target element is found in the first comparison.

```text
O(1)
```

### Average Case

The search space is halved in every iteration.

```text
O(log n)
```

### Worst Case

The element is found after the maximum number of divisions or is not present.

```text
O(log n)
```

---

## Space Complexity

Only a few variables (`left`, `right`, `mid`) are used.

```text
O(1)
```

---

# 🎯 Key Concepts

* Binary Search
* Divide and Conquer
* Searching in Sorted Arrays
* Two Pointers (`left` and `right`)
* Loop Control (`break`)
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### Target at First Position

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

### Target at Last Position

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

### Target Not Present

Input

```text
5
10 20 30 40 50
35
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

# ⚠️ Important Notes

* Binary Search **requires the array to be sorted**.
* If the array is unsorted, the algorithm may return incorrect results.
* Each iteration reduces the search space by half, making Binary Search much faster than Linear Search for large sorted arrays.

---

# 🧩 Pattern

**Pattern:** Binary Search

This algorithm uses the **Divide and Conquer** technique by repeatedly reducing the search space into two halves.

---

# 📚 Related Problems

* Search Insert Position
* First Bad Version
* Guess Number Higher or Lower
* Find First and Last Position of Element
* Peak Element
* Search in Rotated Sorted Array
* Find Minimum in Rotated Sorted Array

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* When Binary Search can be used.
* Why the array must be sorted.
* How to maintain `left`, `right`, and `mid`.
* How Binary Search reduces the search space.
* Why Binary Search runs in **O(log n)** time.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms
