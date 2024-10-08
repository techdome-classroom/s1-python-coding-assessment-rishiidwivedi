class Solution:
   
def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(grid, i, j):
       
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return
        
       
        grid[i][j] = 'W'
        
        
        dfs(grid, i + 1, j)  # down
        dfs(grid, i - 1, j)  # up
        dfs(grid, i, j + 1)  # right
        dfs(grid, i, j - 1)  # left
    
    islands = 0
   
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L': 
                islands += 1
                dfs(grid, i, j) 
    
    return islands
   
                    
     
