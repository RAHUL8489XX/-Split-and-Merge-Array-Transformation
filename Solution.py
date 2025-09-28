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
            # Try all possible subarrays to split and reinsert
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

        return -1  # Should never reach here if nums2 is a permutation of nums1
