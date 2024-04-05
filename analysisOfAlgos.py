# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Min Max using Divide and Conquer
def min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    else:
        mid = len(arr) // 2
        min1, max1 = min_max(arr[:mid])
        min2, max2 = min_max(arr[mid:])
        return min(min1, min2), max(max1, max2)

# Fractional Knapsack
def fractional_knapsack(weights, values, capacity):
    ratios = [(values[i] / weights[i], i) for i in range(len(weights))]
    ratios.sort(reverse=True)
    max_value = 0
    fractions = [0] * len(weights)
    for ratio, i in ratios:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity / weights[i]
            max_value += values[i] * fractions[i]
            break
    return max_value, fractions

# Job Sequencing
def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort jobs by profit in descending order
    max_deadline = max(jobs, key=lambda x: x[1])[1]  # Find max deadline
    print("max deadline: ", max_deadline)
    slots = [-1] * max_deadline
    for job in jobs:
        deadline = job[1] - 1
        while deadline >= 0:
            if slots[deadline] == -1:
                slots[deadline] = job[0]
                break
            deadline -= 1
    return [job for job in slots if job != -1]

# Prim's Algorithm
def prims_algorithm(graph):
    vertices = set(graph.keys())
    mst = []
    if vertices:
        start_vertex = vertices.pop()
        mst.append(start_vertex)
        while vertices:
            min_edge = None
            for vertex in mst:
                for neighbor, weight in graph[vertex].items():
                    if neighbor in vertices and (min_edge is None or weight < min_edge[1]):
                        min_edge = (neighbor, weight, vertex)
            if min_edge:
                mst.append(min_edge[0])
                vertices.remove(min_edge[0])
    return mst

# Kruskal's Algorithm
class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        self.parent[self.find(vertex1)] = self.find(vertex2)

def kruskals_algorithm(vertices, edges):
    mst = []
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(vertices)
    for edge in edges:
        vertex1, vertex2, weight = edge
        if uf.find(vertex1) != uf.find(vertex2):
            mst.append(edge)
            uf.union(vertex1, vertex2)
    return mst

# Dijkstra's Algorithm
import heapq

def dijkstras_algorithm(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_distance, curr_vertex = heapq.heappop(pq)
        if curr_distance > distances[curr_vertex]:
            continue
        for neighbor, weight in graph[curr_vertex].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Floyd Warshall's Algorithm
def floyd_warshall(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}
    for u in vertices:
        dist[u][u] = 0
        for v, w in graph[u].items():
            dist[u][v] = w
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Bellman Ford Algorithm
def bellman_ford(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                return "Graph contains negative weight cycle"
    return distances

# Longest Common Subsequence (LCS) Algorithm
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs_sequence = [""] * (index + 1)
    lcs_sequence[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_sequence)

# N-Queens Problem
def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, col, N, result):
    if col == N:
        result.append([''.join(str(cell) for cell in row) for row in board])
        return
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, result)
            board[i][col] = 0

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)
    return result

# Naive String Matching Algorithm
def naive_string_matching(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)
    return matches


if __name__ == "__main__":
    # Testing each function with sample inputs
    arr = [64, 25, 12, 22, 11]
    print("Selection Sort:", selection_sort(arr[:]))
    print("Insertion Sort:", insertion_sort(arr[:]))
    print("Merge Sort:", merge_sort(arr[:]))
    print("Quick Sort:", quick_sort(arr[:]))
    print("Binary Search:", binary_search(arr[:], 22))
    print("Min Max using Divide and Conquer:", min_max(arr[:]))
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    print("Fractional Knapsack:", fractional_knapsack(weights, values, capacity))
    jobs = [(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25), (6, 2, 20)]
    print("Job Sequencing:", job_sequencing(jobs))
    graph = {
        'A': {'B': 2, 'D': 4},
        'B': {'A': 2, 'C': 3, 'D': 1},
        'C': {'B': 3, 'D': 5},
        'D': {'A': 4, 'B': 1, 'C': 5}
    }
    print("Prim's Algorithm:", prims_algorithm(graph))
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B', 2), ('A', 'D', 4), ('B', 'C', 3), ('B', 'D', 1), ('C', 'D', 5)]
    print("Kruskal's Algorithm:", kruskals_algorithm(vertices, edges))
    graph = {
        'A': {'B': 3, 'C': 6},
        'B': {'A': 3, 'C': 2, 'D': 3},
        'C': {'A': 6, 'B': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }
    print("Dijkstra's Algorithm:", dijkstras_algorithm(graph, 'A'))
    graph = {
        'A': {'B': 3, 'C': 6, 'D': float('inf')},
        'B': {'A': 3, 'C': 2, 'D': 1},
        'C': {'A': 6, 'B': 2, 'D': 3},
        'D': {'A': float('inf'), 'B': 1, 'C': 3}
    }
    print("Floyd Warshall's Algorithm:", floyd_warshall(graph))
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'C': 5, 'B': 1},
        'E': {'D': -3}
    }
    print("Bellman Ford Algorithm:", bellman_ford(graph, 'A'))
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Longest Common Subsequence (LCS) Algorithm:", lcs(X, Y))
    print("N-Queens Problem:", solve_n_queens(4))
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    print("Naive String Matching Algorithm:", naive_string_matching(text, pattern))
