# directed BFS
# basic implementation


class BFS:
    def __init__(self):
        self.vertex = {}

    def print(self):
        for i in self.vertex.keys():
            print(i, '--->', ' ---> '.join([str(j) for j in self.vertex[i]]))

    def addEdge(self, source, dest):
        if source in self.vertex.keys():
            self.vertex[source].append(dest)
        else:
            self.vertex[source] = [dest]

    def traverse(self, source):
        visited = [False] * len(self.vertex)
        queue = []
        visited[source] = True
        queue.append(source)
        print("BFS Tracking: ")
        while queue:
            source = queue.pop(0)
            print(source, ' ', end='')
            for i in self.vertex[source]:
                if visited[i] is False:
                    visited[i] = True
                    queue.append(i)


if __name__ == '__main__':
    graph = BFS()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    graph.print()
    print("Breadth first search")
    graph.traverse(2)
