from typing import List
class Solution():
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # check for an empty matrix
        if not matrix:
            return []
        # initialize rows, cols as length of outer list, length of first inner list (must be a square matrix)
        rows, cols = len(matrix), len(matrix[0])
        pacific_reached = set()
        atlantic_reached = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # traverse neighbors
            for dir in directions:
                next_i, next_j = i + dir[0], j + dir[1]
                if 0 <= next_i < rows and 0 <=next_j < cols:
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)
        for row in range(rows):
            traverse(row, 0, pacific_reached)
            traverse(row, cols -1, atlantic_reached)
        for col in range(cols):
            traverse(0, col, pacific_reached)
            traverse(rows-1, col, atlantic_reached)
        return list(pacific_reached & atlantic_reached)







    
    #     # returns True if row is monotonically increasing
    #     # add an index, (e.g. row[i:]), record the last index where true
    #     return 

    # def makeColumns(self, map):
    #     frame = DataFrame(map).transpose()
        
    #     # get columns from dataframe
    #     return frame
# could flip dataframe all four directions and run monotonicity check on each
# monotonicity check has to return index up to which it is true 
# all edge positions only have to check opposite direction of edge
               
s = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
test = s.pacificAtlantic(heights)
print(test)

