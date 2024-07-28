# Naloga 3: Butale
# Emina Merlak Susman, 272151132
# Praktična matematika, 3. letnik

m, n = map(int, input().split())

while m != 0 and n != 0:
    grid = []
    player_index = [(1, 1), 0]
    end_index = [(1, 1), 0]

    # getting input for grid
    for i in range(n):
        row = input().split()
        grid.append(row)
        try:
            y_ind = row.index('2')
        except ValueError:
            y_ind = -1

        if y_ind != -1:
            y_ind = row.index('2')
            x_ind = i
            player_index = [(x_ind, y_ind), 0]

        try:
            y_ind = row.index('3')
        except ValueError:
            y_ind = -1

        if y_ind != -1:
            y_ind = row.index('3')
            x_ind = i
            end_index = [(x_ind, y_ind), 0]


    def find_reachable_points(pos, deleted_walls, grid, n, m):
        '''find reachable points from pos'''

        dist = pos[1]

        pt_left = pos
        pt_right = pos
        pt_up = pos
        pt_down = pos

        # moving up until you hit a wall or end of grid
        row = pt_up[0][0]
        col = pt_up[0][1]
        while row-1 >= 0 and (grid[row-1][col] != '1' or (row-1, col) in deleted_walls):
            pt_up = [(row - 1, col), dist+1]
            row = pt_up[0][0]
            col = pt_up[0][1]

        # moving down until you hit a wall or end of grid
        row = pt_down[0][0]
        col = pt_down[0][1]
        while row+1 < n and (grid[row+1][col] != '1' or (row + 1, col) in deleted_walls):
            pt_down = [(row + 1, col), dist+1]

            row = pt_down[0][0]
            col = pt_down[0][1]

        # moving left until you hit a wall or end of grid
        row = pt_left[0][0]
        col = pt_left[0][1]
        while col - 1 >= 0 and (grid[row][col-1] != '1' or (row, col-1) in deleted_walls):
            pt_left = [(row, col-1), dist+1]

            row = pt_left[0][0]
            col = pt_left[0][1]

        # moving right until you hit a wall or end of grid
        row = pt_right[0][0]
        col = pt_right[0][1]
        while col + 1 < m and (grid[row][col + 1] != '1' or (row, col + 1) in deleted_walls):
            pt_right = [(row, col+1), dist+1]

            row = pt_right[0][0]
            col = pt_right[0][1]

        reachable_points = [pt_down, pt_up, pt_left, pt_right]
        return reachable_points


    def solve():

        checked_pts = [(player_index, 0)]  # the second number is the direction that the point came from
        dist = 0
        deleted_walls_list = [[(player_index, 0)]]

        while len(checked_pts) > 0 and dist <= 10:
            next = checked_pts.pop(0)
            point_to_check = next[0]

            # list of deleted walls
            deleted_walls = deleted_walls_list.pop(0)

            reachable_pts = find_reachable_points(point_to_check, deleted_walls, grid, n, m)  # neighbours

            for i in range(len(reachable_pts)):
                pt = reachable_pts[i]
                direction = i + 1
                x = pt[0][0]
                y = pt[0][1]
                dist = pt[1]

                if dist == 10 and grid[x][y] != '3':
                    continue

                if grid[x][y] == '3':
                    print(dist)
                    return dist

                if pt != point_to_check:
                    checked_pts.append((pt, direction))

                    # update list of deleted walls by adding wall that was deleted by this move
                    row = x
                    col = y

                    deleted_walls_latest = list(deleted_walls)
                    if direction == 1:  # means we came from downward move, delete wall below this point
                        if row + 1 < n:
                            wall = (row + 1, col)
                            deleted_walls_latest.append(wall)

                    elif direction == 2:  # means we came from upnward move, delete wall above this point
                        if row - 1 >= 0:
                            wall = (row - 1, col)
                            deleted_walls_latest.append(wall)

                    elif direction == 3:  # means we came from left move, delete wall to the right
                        if col - 1 >= 0:
                            wall = (row, col - 1)
                            deleted_walls_latest.append(wall)

                    if direction == 4:  # means we came from right move, delete wall to  the left
                        if col + 1 < m:
                            wall = (row, col + 1)
                            deleted_walls_latest.append(wall)

                    deleted_walls_list.append(deleted_walls_latest)
        print(-1)

        return -1

    solve()

    m, n = map(int, input().split())