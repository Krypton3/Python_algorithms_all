# directed dfs
# basic implementation


class DFS:
    def __init__(self):
        self.vertex = {}

    def addEdge(self, source, dest):
        if source in self.vertex.keys():
            self.vertex[source].append(dest)
        else:
            self.vertex[source] = [dest]

    def print(self):
        for i in self.vertex.keys():
            print(i, '--->', ' ---> '.join([str(j) for j in self.vertex[i]]))

    def search_nodes(self, source, visited):
        visited[source] = True
        print(source)

        for i in self.vertex[source]:
            if visited[i] is False:
                self.search_nodes(i, visited)

    def traverse(self, source):
        visited = [False] * len(self.vertex)
        print("Depth First Search Tracking: \n")
        self.search_nodes(source, visited)


if __name__ == '__main__':
    graph = DFS()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    graph.print()
    print("Depth first search")
    graph.traverse(2)
