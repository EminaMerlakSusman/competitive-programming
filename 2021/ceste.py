# Domača naloga 4: Ceste
# Emina Merlak Susman, 27151132
# praktična matematika, 3. letnik

T = int(input())

for _ in range(T):
    l = input()
    n, m, s, t = map(int, input().split())
    C, D = map(int, input().split())

    graph = [[] for _ in range(n)]

    # roads
    for i in range(m):
        u, v, c, d, h = map(int, input().split())
        edge = (v-1, c, d, h)
        graph[u-1].append(edge)

    # finding all paths between s and t

    queue = [s-1]
    visited = [False for i in range(n)]
    height_each_node = [10**9 for i in range(n)] # all have infinite distance
    price_each_node = [10**9 for i in range(n)]
    length_each_node = [10**9 for i in range(n)]

    height_each_node[s - 1] = 0
    price_each_node[s - 1] = 0
    length_each_node[s - 1] = 0

    found = []
    while queue:
        curr = queue.pop()
        if not visited[curr]:

            # costs up to current node
            height_before = height_each_node[curr]
            length_before = length_each_node[curr]
            price_before = price_each_node[curr]

            for neighbour in graph[curr]:
                    if not visited[neighbour[0]]:
                        height_now = height_before + neighbour[3]
                        length_now = length_before + neighbour[2]
                        price_now = price_before + neighbour[1]

                        cost_this_path = (height_now, length_now, price_now)

                        if height_now <= height_each_node[neighbour[0]] and price_now <= C and length_now <= D:
                            height_each_node[neighbour[0]] = height_now

                            if price_now <= price_each_node[neighbour[0]]:
                                price_each_node[neighbour[0]] = price_now

                            if length_now <= length_each_node[neighbour[0]]:
                                length_each_node[neighbour[0]] = length_now

                        if neighbour[0] == t-1:
                            #if height_now <= height_each_node[neighbour[0]] and price_now <= C and length_now <= D:
                            found.append((height_now, price_now, length_now))


                        queue.append(neighbour[0])

            visited[curr] = True


    if len(found) == 0:
        print(-1)
    else:
         found = sorted(found)

         #if found[0] in [(0, 11, 0), (0, 28, 2), (10, 1, 1), (9, 2, 2), (0, 17, 0)]:
            #print(found)
         print(found[0][0], found[0][1], found[0][2])


