graph = {
  "A": ["B", "C"],
  "B": ["A", "D"],
  "C": ["A", "D"],
  "D": ["B", "C"]

} # adjancecy list


def dfs(startNode):
  stack = [startNode]
  visited = {}

  while len(stack) > 0:
    currentVertex = stack.pop()

    if currentVertex not in visited :
      visited[currentVertex] = True
      print(currentVertex)

      for neibghbour in graph[currentVertex]:
        stack.append(neibghbour)

#dfs("A")



def bfs(startNode):
  queue = [startNode]
  visited = {}

  while len(queue) > 0:
    currentVertex = queue.pop(0)

    if currentVertex not in visited :
      visited[currentVertex] = True
      print(currentVertex)

      for neibghbour in graph[currentVertex]:
        queue.append(neibghbour)


bfs("A")