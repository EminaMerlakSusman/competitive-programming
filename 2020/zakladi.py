# Emina Merlak Susman
# Praktična matematika
# 27151132


#import tarjan
#import time
#import sys
#sys.setrecursionlimit(sys.maxsize)
#print(sys.getrecursionlimit())


#st = time.time()
#file = open('zakladi(1)/zakladi05.in', 'r')


N, M = map(int, input().split())
#N, M = map(int, input().split())

graph = {}

for k in range(1, N + 1):
    graph[k] = []

edges = []

for k in range(M):
    line = tuple(map(int, input().split()))
    #line = tuple(map(int, file.readline().split()))
    node1 = line[0]
    node2 = line[1]
    weight = line[2]
    graph[node1].append((node2, weight))
    edges.append((node1, node2, weight))




# graph_no_weights = {}
# for node, pts in graph.items():
#     pts2 = [x[0] for x in pts]
#     graph_no_weights[node] = pts2

#print('1', graph_no_weights)
#components = tarjan.tarjan(graph_no_weights)



# A function used by DFS
def DFSUtil(graph, v, visited, comp):
    # Mark the current node as visited and print it

    visited[v] = True
    comp.append(v)
    # print(v)
    # Recur for all the vertices adjacent to this vertex
    for i in graph[v]:
        if visited[i[0]] == False:

            DFSUtil(graph, i[0], visited, comp)
    return comp


def fillOrder(graph, v, visited, stack):
    # Mark the current node as visited
    visited[v] = True
    # Recur for all the vertices adjacent to this vertex
    for i in graph[v]:
        # print(i)
        if visited[i[0]] == False:
            fillOrder(graph, i[0], visited, stack)
    stack.append(v)


# Function that returns reverse (or transpose) of this graph
def getTranspose(graph):
    g = {}
    for i in graph.keys():
        g[i] = []

    # Recur for all the vertices adjacent to this vertex
    for i, neighbours in graph.items():
        for j in neighbours:
            #g.addEdge(j, i)
            g[j[0]].append((i, j[1]))

    return g

# The main function that finds and prints all strongly
# connected components
def printSCCs(graph):

    stack = []
    # Mark all the vertices as not visited (For first DFS)

    visited = [False] * (N + 1)
    # put nodes in stack according to their finishing
    # times
    for i in range(1, N + 1):
        if visited[i] == False:
            fillOrder(graph, i, visited, stack)

    # transpose graph
    gr = getTranspose(graph)

    # preparing second DFS
    visited = [False] * (N + 1)

    # processing nodes in stack
    comps = []
    indexes_comps = [0] * (N + 1)
    while stack:
        i = stack.pop()

        if visited[i] == False:

            a = DFSUtil(gr, i, visited, [])

            comps.append(a)
            for nd in a:
                indexes_comps[nd] = len(comps)

    return (comps, indexes_comps)

fun = printSCCs(graph)
indexes_comps = fun[1]
#print('indexes_comps', indexes_comps)
comps = fun[0]
# comps2 = tarjan.tarjan(graph_no_weights)
# count = 0
# for i in range(len(comps)):
#     comp = comps[i]
#     if comp == comps2[i]:
#         count += 1

#print(comps == comps2)
#print(comps)
#print(comps2)
# print(indexes_comps)

prices_comps = [0] * (len(comps) + 1)
degs = [0] * (len(comps) + 1) # outgoing vertices for each component
#print('edges', edges)

outgoing = [[] for _ in range(N + 1)] # incoming and outgoing edges for each vertex
incoming = [[] for _ in range(N + 1)]

for i in range(len(edges)):
    edge = edges[i]
    #print('edge:', edge)
    a = edge[0]
    b = edge[1]
    c = edge[2]
    if indexes_comps[a] == indexes_comps[b]:
        #print('edge inside same component found:', a, b)
        prices_comps[indexes_comps[a]] += c
    else:
        #print(a, b)
        #print(indexes_comps[b])
        degs[indexes_comps[a]] += 1

        incoming[b].append(i)
        #rint(incoming)
        outgoing[a].append(i)
    #print(outgoing)

#print('degs', degs)
#print(prices_comps, len(prices_comps))
#print(degs)
queue = []

for i in range(1, len(comps) + 1):
    if degs[i] == 0: # we first check the components at the end of the path, i.e. ones with no outgoing edges
        queue.append(i)

while len(queue) != 0:
    comp_id = queue.pop()
    max_cost = 0

    comp = comps[comp_id - 1]
    #print('processing component:', comp)
    for i in range(len(comp)):
        node = comp[i]
        #print('node:', node)
        out_list = outgoing[node]
        #print('outgoing:', out_list)
        # for this component, finding maximum-cost outgoing edge

        for ind in out_list:
            edg = edges[ind]
            #print('edge:', edg)
            b = edg[1]
            c = edg[2]
            b_comp = indexes_comps[b]
            #print('b belongs to:', b_comp, b_comp == comp_id)
            if b_comp != comp_id:
                #print('cost:', c)
                if prices_comps[b_comp] + c > max_cost: # if prices found until now + cost of this edge is bigger than
                    max_cost = prices_comps[b_comp] + c # current maximum, update maximum
                    #print('max cost:', max_cost)


        # decreasing degree of incoming edges to this component
        # once an incoming component's degree reaches zero, it
        # means it has been reached by the path and it can be added to the queue
        in_list = incoming[node]
        for ind in in_list:
            edg = edges[ind]
            a = edg[0] # node where the edge is coming from
            c = edg[1]
            a_comp = indexes_comps[a]
            if a_comp != comp_id:
                degs[a_comp] -= 1
                if degs[a_comp] == 0:
                    queue.append(a_comp)


    prices_comps[comp_id] += max_cost

#sol = open('zakladi(1)/zakladi04.out', 'r')
for i in range(1, N + 1):
    #s = int(sol.readline())
    #print(prices_comps[indexes_comps[i]] == s)
    print(prices_comps[indexes_comps[i]])

#end = time.time() - st
#print(end)