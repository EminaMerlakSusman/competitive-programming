#Emina Merlak Susman,
#27151132
#Naloga 3: Cevovod

from typing import List, Tuple

def find_longest_path(t: int, cases: List[Tuple[int, int, List[Tuple[int, int, int]], int, int]]) -> List[int]:
    results = []
    for n, m, edges, s, f in cases:
        # Initialize data structures
        vtx = [[] for _ in range(501)]
        arr = []
        dist = [0] * 555
        dq = []
        deg = [0] * 555
        s=s-1
        f=f-1
        
        # Read in edges and update vtx, deg
        for u, v, c in edges:
            u -= 1
            v -= 1
            vtx[u].append((v, c))
            deg[v] += 1
        
        # Add nodes with no incoming edges to the deque
        for i in range(n):
            if deg[i] == 0:
                dq.append(i)
        
        # Perform topological sort
        al = 0
        while dq:
            cnt = len(dq)
            for i in range(cnt):
                arr.append(dq[0])
                for v, c in vtx[dq[0]]:
                    if deg[v] == 0:
                        dq.append(v)
                    deg[v] -= 1
                dq.pop(0)
        
        # Find the index of the starting node in the sorted list
        idx = 0
        while idx < len(arr) and arr[idx] != s:
            idx += 1
        if idx == len(arr):
            results.append(-1)
        else:
            # Calculate the longest path from the starting node
            for i in range(idx, len(arr)):
                for v, c in vtx[arr[i]]:
                    dist[v] = max(dist[v], dist[arr[i]] + c)
    
            if dist[f] == 0:
                results.append(-1)
            else:
                results.append(dist[f])
    return results

# Read the number of test cases
t = int(input())

# Initialize the list of test cases
cases = []

# Read the test cases
for _ in range(t):
    ln = input()
    # Read the number of nodes and edges
    n, m = map(int, input().split())
    
    # Read the edges
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    
    # Read the starting and ending nodes
    s, f = map(int, input().split())
    
    # Add the test case to the list
    cases.append((n, m, edges, s, f))

# Find the longest path in each case
results = find_longest_path(t, cases)

# Print the results
for result in results:
    print(result)