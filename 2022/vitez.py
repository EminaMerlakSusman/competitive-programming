#import time
# Emina Merlak Susman, 27151132
# Praktična matematika, 3. letnik
# Vitez in zmaj
class Queue:
 
    def __init__(self):
        self.elements = []
 
    def enqueue(self,val):
        self.elements.append(val)
 
    def dequeue(self):
        val = None
        try:
            val = self.elements[0]
            if len(self.elements) == 1:
                self.elements = []
            else:
                self.elements = self.elements[1:]
        except:
            pass
 
        return val
 
    def IsEmpty(self):
        result = False
        if len(self.elements) == 0:
            result = True
        return result
 
    def get_elts(self):
        return self.elements
 
 
path_queue = Queue()
 
 
def bfs(graph, dimensions, start, end, end_coords, q, l):
    '''Return all possible paths of length up to l between start and end nodes in undirected graph of dimensions 'dimensions'.'''
    diff = end_coords[1][0] - end_coords[0][0] + end_coords[1][1] - end_coords[0][1] - 1
    if diff > l:
        return []
 
    valid_paths = []
    temp_path = [start]
    q.enqueue(temp_path)
    while q.IsEmpty() == False:
        tmp_path = q.dequeue()
        if len(tmp_path) == l + 3:
            break
 
        last_node = tmp_path[len(tmp_path)-1]
        if last_node == end:
            valid_paths.append(tmp_path)
            continue
 
 
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)
 
    return valid_paths
 
def steps_in_same_dir(path):
    '''Finds number of steps in the same direction'''
    i = 1
    path = path[:-1]
    if len(path) > 2:
        diff = path[-i] - path[-i-1]
        while path[-i-1] - path[-i-2] == diff:
            i += 1
        return i
    elif len(path) == 2:
        return 1
    else:
        return 0
 
 
n = int(input())
results = []
for _ in range(n):
    #getting graph
    empty_line = input()
    w, h, l = map(int, input().split())
    lines = []
    dimensions = (w, h)
    for i in range(h):
        line = input()
        lines.append(line)
 
    #st_time = time.time()
    #getting adjacency list for graph
    graph = []
    end_coords = []
    for i in range(h):
        for j in range(w):
            elt = lines[i][j]
            elt_ind = w*i + j
            neighbours = []
 
            #checking for start and end nodes
            if elt == 'V':
                end_coords.append((i,j))
                start = elt_ind
            elif elt == 'Z':
                end_coords.append((i,j))
                end = elt_ind
 
            #getting neighbours
            if elt in '.VZ':
                if j + 1 < w and lines[i][j + 1] in '.VZ':
                    index = (w*i) + (j + 1)
                    neighbours.append(index)
                if i + 1 < h and lines[i+1][j] in '.VZ':
                    index = (w * (i+1)) + j
                    neighbours.append(index)
                if j - 1 >= 0 and lines[i][j - 1] in '.VZ':
                    index = (w*i) + (j - 1)
                    neighbours.append(index)
                if i - 1 >= 0 and lines[i-1][j] in '.VZ':
                    index = (w * (i-1)) + j
                    neighbours.append(index)
            graph.append(neighbours)
 
    paths = bfs(graph, dimensions, start, end, end_coords, path_queue, l)
    strength = 0
 
    for path in paths:
        path = list(map(int, path))
        stps = steps_in_same_dir(path)
        if stps > strength:
            strength = stps
    if len(paths) == 0:
        results.append(0)
    else:
        results.append(strength + 1)
 
for r in results:
    print(r)
#print("--- %s seconds ---" % (time.time() - st_time))