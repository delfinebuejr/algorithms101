import pprint

def AddEdge(adjList, u, v):
    adjList[u].append(v)

def main():
  vertices = 5

  adjList = [ [] for _  in range(vertices) ]

  AddEdge(adjList, 0, 1)
  AddEdge(adjList, 0, 2)
  AddEdge(adjList, 2, 3)
  AddEdge(adjList, 1, 3)
  AddEdge(adjList, 3, 4)

  pprint.pp(adjList)


  ## adjList via dictionary

  adjList2 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"]
  }

  pprint.pp(adjList2)

main()