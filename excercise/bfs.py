from collections import deque

# adjList - what data do i process?
# startnode - where do i start?
# visited - which vertices have been visited?

def bfs(adjList, startnode, visited):
  q = deque()

  # start processing from the startnode
  visited[startnode] = True
  q.append(startnode)

  # loop while the q has vertices in it
  while q:
    # process the vertice node
    currentnode = q.popleft()
    print("current node:", end=" ")

    # get the neighbor of the last processed vertice
    for neighbor in adjList[currentnode]:
      # add the discovered neighbor/s to the queue for processing
      # only if it is not visited
      if not visited[neighbor] == True:
        q.append(neighbor)
