class Solution:
    def minPathSum(self, grid):
        def min_path_to(x, y):
            if x == y == 0:
                visited[0][0] = grid[0][0]
                return visited[0][0]

            if visited[x][y] == -1:
                left = large_int if x == 0 else min_path_to(x-1, y)
                top = large_int if y == 0 else min_path_to(x, y-1)
                visited[x][y] = min(left, top) + grid[x][y]

            return visited[x][y]

        large_int = 999999999
        grid_height = len(grid)
        grid_width = len(grid[0])
        visited = [[-1]*grid_width for _ in range(grid_height)]
        return min_path_to(grid_height-1, grid_width-1)


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    solution = Solution()
    print(solution.minPathSum(grid))
    #assert solution.minPathSum(grid) == 7

    print('Test Passed!!')
