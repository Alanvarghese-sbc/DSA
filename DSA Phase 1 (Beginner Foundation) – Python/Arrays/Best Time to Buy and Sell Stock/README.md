# Best Time to Buy and Sell Stock

## 📌 Problem Statement

You are given an array where each element represents the stock price on a particular day.

You are allowed to:

* Buy the stock **only once**
* Sell the stock **only once**
* You must **buy before you sell**

Find and print the **maximum profit** that can be earned.

If no profit can be made, print **0**.

---

# Example 1

### Input

```text
6
7 1 5 3 6 4
```

### Output

```text
5
```

### Explanation

* Buy at price **1**
* Sell at price **6**

Profit = **6 − 1 = 5**

---

# Example 2

### Input

```text
5
7 6 4 3 1
```

### Output

```text
0
```

### Explanation

Stock prices continuously decrease, so no profit can be made.

---

# Example 3

### Input

```text
6
2 4 1 7 5 9
```

### Output

```text
8
```

### Explanation

* Buy at **1**
* Sell at **9**

Profit = **8**

---

# 💡 Approach

Traverse the array only once while keeping track of:

* **minimum_price** → The lowest stock price encountered so far.
* **max_profit** → The highest profit found so far.

For each day's price:

* If it is lower than the current minimum price, update the minimum price.
* Otherwise, calculate the profit by selling on the current day.
* Update the maximum profit if the current profit is greater.

---

# 🧠 Algorithm

1. Read the number of days.
2. Read the stock prices.
3. Initialize:

   * `minimum_price = arr[0]`
   * `max_profit = 0`
4. Traverse the array from the second element.
5. If the current price is smaller than `minimum_price`, update it.
6. Otherwise:

   * Calculate the current profit.
   * Update `max_profit` if necessary.
7. Print the maximum profit.

---

# 💻 Python Solution

```python
n = int(input())

arr = list(map(int, input().split()))

minimum_price = arr[0]
max_profit = 0

for i in range(1, n):
    if arr[i] < minimum_price:
        minimum_price = arr[i]
    else:
        profit = arr[i] - minimum_price

        if profit > max_profit:
            max_profit = profit

print(max_profit)
```

---

# ▶️ Dry Run

### Input

```text
7 1 5 3 6 4
```

| Day | Price | Minimum Price | Profit | Maximum Profit |
| --: | ----: | ------------: | -----: | -------------: |
|   1 |     7 |             7 |      - |              0 |
|   2 |     1 |             1 |      - |              0 |
|   3 |     5 |             1 |      4 |              4 |
|   4 |     3 |             1 |      2 |              4 |
|   5 |     6 |             1 |      5 |              5 |
|   6 |     4 |             1 |      3 |              5 |

Final Output

```text
5
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

Only a few variables are used.

```text
O(1)
```

---

# 🎯 Key Concepts

* Arrays
* Greedy Algorithm
* Array Traversal
* Running Minimum
* Maximum Profit
* Time Complexity
* Space Complexity

---

# 🚨 Edge Cases

### Prices Always Increase

**Input**

```text
5
1 2 3 4 5
```

**Output**

```text
4
```

---

### Prices Always Decrease

**Input**

```text
5
5 4 3 2 1
```

**Output**

```text
0
```

---

### Single Day

**Input**

```text
1
5
```

**Output**

```text
0
```

---

### Same Price Every Day

**Input**

```text
5
3 3 3 3 3
```

**Output**

```text
0
```

---

# 🧩 Pattern

**Pattern:** Greedy / Running Minimum

Maintain the smallest stock price seen so far while traversing the array. At each step, calculate the profit that would be earned by selling on the current day and update the maximum profit if it is larger.

---

# 📚 Related Problems

* Best Time to Buy and Sell Stock II
* Best Time to Buy and Sell Stock III
* Maximum Subarray Sum (Kadane's Algorithm)
* Maximum Difference Between Two Elements
* Container With Most Water

---

# 📝 Learning Outcome

After solving this problem, you should understand:

* How to solve optimization problems using a greedy approach.
* How to maintain a running minimum during array traversal.
* Why a single-pass solution achieves **O(n)** time complexity.
* How to calculate the maximum possible profit while ensuring the stock is bought before it is sold.

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Python | Data Structures & Algorithms
