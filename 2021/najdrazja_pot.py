# Naloga 2: Najdražja pot
# Emina Merlak Susman, 27151132
# praktična matematika, 3. letnik


from _collections import deque
import sys

global checked_nodes


def solve():
    # method return farthest node and its distance from node u
    def BFS(G, u, distance, n):
        # marking all nodes as unvisited
        visited_3 = [False for i in range(n)]
        # mark all distance with -1
        global checked_nodes
        queue = deque()
        queue.append(u)
        # mark node u as visited
        visited_3[u] = True

        #if checked_nodes != n:
        checked_nodes += 1
        maxDis = 0
        nodeIdx = 0
        while queue:

            # pop the front of the queue(0th element)
            front = queue.popleft()
            # loop for all adjacent nodes of node front

            for i, w in G[front]:
                if not visited_3[i]:
                    # mark the ith node as visited
                    visited_3[i] = True

                    checked_nodes += 1
                    # make distance of i , one more than distance of front

                    distance[i] += distance[front] + w

                    # get farthest node distance and its index
                    if distance[i] > maxDis:
                        maxDis = distance[i]
                        nodeIdx = i
                    # Push node into the stack only if it is not visited already
                    queue.append(i)

        # print(distance)
        return nodeIdx, maxDis
    global checked_nodes

    n, m = map(int, sys.stdin.readline().strip().split())
    prices = list(map(int, sys.stdin.readline().strip().split()))  # prices of vertices

    G = [[] for i in range(n)]
    G_inv = [[] for i in range(n)]

    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        G[a - 1].append((b - 1, c))
        G[b - 1].append((a - 1, c))

    # print(n)

    distance = [i for i in prices]

    checked_nodes = 0
    max_cost = 0
    initial_cost = prices
    while checked_nodes < n//2:
        endpoint, cost_1 = BFS(G, checked_nodes, distance, n)
        startpoint, cost = BFS(G, endpoint, initial_cost, n)
        if cost > max_cost:
            max_cost = cost
        checked_nodes //= 2
    print(cost)

k = int(sys.stdin.readline())
for i in range(k):
    ln = sys.stdin.readline()
    solve()
