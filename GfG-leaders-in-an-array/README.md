# Leaders in an Array

## Problem Statement

Given an array `arr` of positive integers, find all the **leaders** in the array.

An element is considered a **leader** if it is greater than or equal to all the elements to its right. The rightmost element is always a leader.

---

## Examples

### Example 1

**Input:**

```python
arr = [16, 17, 4, 3, 5, 2]
```

**Output:**

```python
[17, 5, 2]
```

**Explanation:**

* 17 is greater than all elements to its right.
* 5 is greater than all elements to its right.
* 2 is the last element, so it is always a leader.

---

### Example 2

**Input:**

```python
arr = [10, 4, 2, 4, 1]
```

**Output:**

```python
[10, 4, 4, 1]
```

**Explanation:**

A leader can be equal to elements on its right. Therefore, both occurrences of 4 are leaders.

---

### Example 3

**Input:**

```python
arr = [5, 10, 20, 40]
```

**Output:**

```python
[40]
```

**Explanation:**

The array is strictly increasing, so only the last element is a leader.

---

### Example 4

**Input:**

```python
arr = [30, 10, 10, 5]
```

**Output:**

```python
[30, 10, 10, 5]
```

**Explanation:**

The array is non-increasing, so every element is a leader.

---

## Constraints

```python
1 <= arr.size() <= 10^6
0 <= arr[i] <= 10^6
```

---

## Approach

Traverse the array from right to left while maintaining the maximum element seen so far.

1. Initialize `max_so_far` with a very small value.
2. Start from the last element.
3. If the current element is greater than or equal to `max_so_far`, it is a leader.
4. Update `max_so_far`.
5. Store all leaders and reverse the result at the end.

---

## Python Solution

```python
class Solution:
    def leaders(self, arr):
        leaders = []
        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_so_far:
                leaders.append(arr[i])
                max_so_far = arr[i]

        return leaders[::-1]
```

---

## Complexity Analysis

* Time Complexity: `O(n)`
* Space Complexity: `O(k)`

where `k` is the number of leaders stored in the output list.
