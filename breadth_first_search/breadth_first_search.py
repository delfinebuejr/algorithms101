# requires:
# understanding of graph


from collections import deque
import pprint, pickle
 

def bfs(adjList, startnode, visited):
  q = deque()

  # mark the visited node
  visited[startnode] = True
  q.append(startnode)

  # process the queue
  while q:
    currentNode = q.popleft()
    print(currentNode, end=" ")

    for neighbor in adjList[currentNode]:
      if not visited[neighbor]:
        visited[neighbor] = True
        q.append(neighbor)

def AddEdge(adjList, u, v):
  adjList[u].append(v)
  

def main():
  
  vertices = 5

  adjList = [ [] for _ in range(vertices) ]

  AddEdge(adjList, 0, 1)
  AddEdge(adjList, 0, 2)
  AddEdge(adjList, 1, 3)
  AddEdge(adjList, 1, 4)  
  AddEdge(adjList, 2, 4)

  print(type(adjList))
  pprint.pp(adjList)

  visited = [False] * vertices

  print("Breadth First Traversal starting from vertex 0:", end=" ")
  bfs(adjList, 0, visited)

  pprint.pp(visited)

#if __name__ == "__main__":
main()