from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        for row in heights:
            row.append('A')
            row.insert(0, 'P')
        heights.append(['A'] * len(row))
        heights.insert(0, ['P'] * len(row))
        return heights

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

s = Solution()
print(s.pacificAtlantic(heights))