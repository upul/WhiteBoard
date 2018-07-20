def unique_paths(m, n):
    def unique_paths_to_xy(x, y):
        if x == y == 0:
            return 1
        if grid[x][y] == 0:
            right = 0 if y == 0 else unique_paths_to_xy(x, y-1)
            bottom = 0 if x == 0 else unique_paths_to_xy(x-1, y)
            grid[x][y] = right + bottom
        return grid[x][y]

    grid = [[0]*n for _ in range(m)]
    return unique_paths_to_xy(m-1, n-1)

def unique_paths_with_obstacles(n, m, obstacles):
    def compute_num_ways(x, y, obstacles):
        if x == y == 0:
            if obstacles[x][y] == 1:
                return 0
            else:
                return 1

        if num_ways[x][y] == 0:
            top = 0 if (x == 0 or obstacles[x][y] == 1) else compute_num_ways(x-1, y, obstacles)
            left = 0 if (y == 0 or obstacles[x][y] == 1) else compute_num_ways(x, y-1, obstacles)
            num_ways[x][y] = top + left
        return num_ways[x][y]

    num_ways = [[0]*m for _ in range(n)] 
    return compute_num_ways(n-1, m-1, obstacles)


if __name__ == '__main__':
    assert unique_paths(2, 2) == 2
    assert unique_paths(3, 2) == 3

    assert unique_paths_with_obstacles(1, 2, [[0, 1]]) == 0
    print('Test Passed!!')
