def num_ways_xy(n, m):
    def compute_num_ways_to_xy(x, y):
        if x == y == 0:
            return 1
        if num_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_num_ways_to_xy(x-1, y)
            ways_left = 0 if y == 0 else compute_num_ways_to_xy(x, y-1)
            num_ways[x][y] = ways_top + ways_left
        return num_ways[x][y]

    num_ways = [[0]*m for _ in range(n)]
    return compute_num_ways_to_xy(n-1, m-1)

def compute_num_ways_to_xy_with_obstacles(n, m, obstacles):
    def compute_num_ways(x, y, obstacles):
        if x == y == 0:
            return 1

        if num_ways[x][y] == 0:
            if obstacles[x][y]:
                return num_ways[x][y]

            top = 0 if x == 0 else compute_num_ways(x-1, y, obstacles)
            left = 0 if y == 0 else compute_num_ways(x, y-1, obstacles)
            num_ways[x][y] = top + left
        return num_ways[x][y]

    num_ways = [[0]*m for _ in range(n)] 
    return compute_num_ways(n-1, m-1, obstacles)
   

if __name__ == '__main__':
    #print(num_ways_xy(5, 5))
    obs = [[False]*4 for _ in range(4)]
    obs[0][2] = True
    obs[1][1] = True
    #obs[3][1] = True
    print(compute_num_ways_to_xy_with_obstacles(4, 4, obs))

    

