#selection sort
def selectionSort(arr):
    for i in range(len(arr)):
        min = float('-inf')
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr
n = int(input("Enter number of elements : "))
arr = list()
for i in range(n):
    arr.append(int(input("Enter element {} : ".format(i+1))))
print("The sorted array is : ")
print(selectionSort(arr))

*Job scheduling* 

profit=[15,27,10,100,150]
jobs=["j1","j2","j3","j4","j5"]
Dead=[2,3,3,3,4]
profitNJobs=list(zip(profit,jobs,Dead))
profitNJobs= sorted(profitNJobs,key=lambda x:x[0],reverse=True)

slot=[]
for i in range(len(jobs)):
    slot.append(0)
    
profit = 0
ans=[]

for i in range(len(jobs)):
    ans.append('null')
    
for i in range(len(jobs)):
    job= profitNJobs[i]
    
    for j in range(job[2],0,-1):
        if slot[j] == 0:
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break
print("job scheduled buddy:",ans[1:])
print(profit)
    

    



#Prims Algorithm    Minimum Spanning Tree

def prim_mst(graph):
    num_vertices = len(graph)
    mst = [None] * num_vertices
    key = [float('inf')] * num_vertices
    visited = [False] * num_vertices

    key[0] = 0
    mst[0] = -1

    for _ in range(num_vertices - 1):
        u = min_key(key, visited)
        visited[u] = True

        for v in range(num_vertices):
            if 0 < graph[u][v] < key[v] and not visited[v]:
                key[v] = graph[u][v]
                mst[v] = u

    return mst

# Helper function to find the vertex with the minimum key value
def min_key(key, visited):
    min_val = float('inf')
    min_idx = -1
    for v in range(len(key)):
        if not visited[v] and key[v] < min_val:
            min_val = key[v]
            min_idx = v
    return min_idx

# Example graph representation
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 4],
    [6, 8, 0, 0, 9],
    [0, 5, 4, 9, 0]
]

mst = prim_mst(graph)
print("Minimum Spanning Tree:")
for i in range(1, len(mst)):
    print(f"Edge: {mst[i]} - {i}\tWeight: {graph[i][mst[i]]}")

