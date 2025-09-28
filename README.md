# 🔄 Split and Merge Array Transformation

Accepted solution for LeetCode Weekly Contest 468 problem:  
[Split and Merge Array Transformation](https://leetcode.com/contest/weekly-contest-468/problems/split-and-merge-array-transformation/)

✅ [View Accepted Submission](https://leetcode.com/contest/weekly-contest-468/problems/split-and-merge-array-transformation/submissions/1778627395/)

---

## 📘 Problem Description

You're given two arrays `nums1` and `nums2`, both of length `n`.  
You can perform the following operation on `nums1` any number of times:

> Choose a subarray `nums1[L..R]`, remove it, and reinsert it (in original order) anywhere in the remaining array.

Your goal is to transform `nums1` into `nums2` using the **minimum number of operations**.

---

## 🧠 Approach

This is a shortest-path problem over permutations of `nums1`.  
We use **Breadth-First Search (BFS)** to explore all valid states by:
- Splitting out every possible subarray.
- Reinserting it at every possible position.
- Tracking visited states to avoid cycles.

The first time we reach `nums2`, we return the number of steps taken.

---

## 💡 Python Solution

```python
from collections import deque

class Solution:
    def minSplitMerge(self, nums1, nums2):
        start = tuple(nums1)
        target = tuple(nums2)
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps

            n = len(curr)
            for i in range(n):
                for j in range(i, n):
                    sub = curr[i:j+1]
                    rest = curr[:i] + curr[j+1:]
                    for k in range(len(rest)+1):
                        new_state = rest[:k] + sub + rest[k:]
                        new_tuple = tuple(new_state)
                        if new_tuple not in visited:
                            visited.add(new_tuple)
                            queue.append((new_tuple, steps + 1))

        return -1  # Should never happen if nums2 is a permutation of nums1
