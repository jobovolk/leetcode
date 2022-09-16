from typing import List
from pandas import DataFrame
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        map = heights[:] 
        # for row in map:
        #     row.append('A')
        #     row.insert(0, 'P')
        # map.append(['A'] * len(row))
        # map.insert(0, ['P'] * len(row))
        return map
    def checkEast(self, row):
        # returns True if row is monotonically increasing
        # add an index, (e.g. row[i:]), record the last index where true
        return all(x<=y for x, y in zip(row, row[1:]))

    def makeColumns(self, map):
        frame = DataFrame(map).transpose()
        
        # get columns from dataframe
        return frame
# could flip dataframe all four directions and run monotonicity check on each
# monotonicity check has to return index up to which it is true 
               

s = Solution()
#%%
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
for row in heights:
    pairs = zip(row, row[1:])
    print(dict(pairs))
    
#%%

map = s.pacificAtlantic(heights)
# print(s.pacificAtlantic(heights))
testEast = s.checkEast(heights[0])
testFrame = s.makeColumns(map)
print(testEast)
for row in map:
    print(row[0])

print(f"{testFrame=} ")
# %%
