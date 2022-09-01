from collections import Counter
from typing import List

class Solution:
    count = 0
    def minSetSize(self, arr: List[int]) -> int:
        total = 0
        frequency_of_entries = sorted(Counter(arr).values(), reverse = True)
    
        for i, v in enumerate(frequency_of_entries):
            total += v
            if total >= len(arr) // 2:
                return i + 1
        return 0


class WebSolution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        sorted_list = sorted(Counter(arr).values(), reverse=True)
        for index, count in enumerate(sorted_list):
            total_count += count
            
            if total_count >= len(arr) // 2:
                return index + 1
        
        return 0

s = Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(s.minSetSize([7,7,7,7,7,7,7,7,7,7,7]))
print(s.minSetSize([3,3,4,3,2,7,5,8,8,8,8,8,8]))

w = WebSolution()
print(w.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(w.minSetSize([7,7,7,7,7,7,7,7,7,7,7]))
print(w.minSetSize([3,3,4,3,2,7,5,8,8,8,8,8,8]))
