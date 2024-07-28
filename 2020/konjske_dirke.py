# Emina Merlak Susman
# Praktična matematika
# 27151132

N = int(input())

chess_grid = []
knight_index = (1, 1)

# getting input for chess grid
for i in range(N):
    row = list(input())
    chess_grid.append(row)
    if '*' in row:
        y_ind = row.index('*')
        x_ind = i
        knight_index = [(x_ind, y_ind), 0]

# getting queries
P = int(input())

indexes = []

for i in range(P):
    l = tuple(map(int, input().split()))
    indexes.append((l[0] - 1, l[1] - 1))



def in_grid(point, N):
    '''Checks if a point is inside a chess grid of dimensions NxN'''
    global chess_grid
    x = point[0]
    y = point[1]
    if (0 <= x < N) and (0 <= y < N) and chess_grid[x][y] not in '#*':
        return True


checked_coords = []

def find_reachable_points(horse, N):
    '''find reachable points from horse'''
    global checked_coords
    row = horse[0][0]
    col = horse[0][1]
    dist = horse[1]
    pt1 = (row - 2, col + 1)
    pt2 = (row - 2, col - 1)
    pt3 = (row + 2, col + 1)
    pt4 = (row + 2, col - 1)
    pt5 = (row + 1, col + 2)
    pt6 = (row - 1, col + 2)
    pt7 = (row - 1, col - 2)
    pt8 = (row + 1, col - 2)
    pt_list = filter(lambda x: in_grid(x, N), [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt7, pt8]) # filter points inside grid
    pt_list = filter(lambda x: x not in checked_coords, pt_list) # checking points that have not been checked yet

    real_list = []
    for pt in pt_list:  # adding distance
        real_list.append([pt, dist+1])
    return real_list



def draw_number(k, point):
    '''Draw number k on the chess grid at reachable point'''
    global chess_grid
    x = point[0]
    y = point[1]
    chess_grid[x][y] = str(k)
    return chess_grid

adj_list_make = {} # making adjacency list of each point, and the points reachable through it
checked_pts = [knight_index]
visited = [[False for i in range(N)] for j in range(N)]
knight_x = knight_index[0][0]
knight_y = knight_index[0][1]
visited[knight_x][knight_y] = True # setting knight as visited

while len(checked_pts) > 0:
    point_to_check = checked_pts.pop(0)
    reachable_pts = find_reachable_points(point_to_check, N) # neighbours

    dist_parent = point_to_check[1]
    for pt in reachable_pts:
            x = pt[0][0]
            y = pt[0][1]
            dist = pt[1]
            if not visited[x][y]:
                visited[x][y] = True
                checked_pts.append(pt)
                draw_number(dist, (x,y))


for pt in indexes:
    x = pt[0]
    y = pt[1]
    dist = chess_grid[x][y]
    if dist not in '.*#':
        print(dist)
    else:
        print(-1)
