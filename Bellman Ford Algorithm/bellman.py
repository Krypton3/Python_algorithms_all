class Bellman:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def make_graph(self, u, v, cost):
        self.graph.append([u, v, cost])

    def BellamFord(self, source):
        distance = [99999] * self.V
        distance[source] = 0

        for i in range(self.V - 1):
            for u, v, cost in self.graph:
                if distance[u] != 99999 and distance[u] + cost < distance[v]:
                    distance[v] = distance[u] + cost

        for u, v, cost in self.graph:
            if distance[u] != 99999 and distance[u] + cost < distance[v]:
                print("This graph contains negative loop!!")
                return

        print("Distance from source to all other vertices: ")
        print("Vertex   Distance")
        for i in range(self.V):
            print("%d        %d" % (i, distance[i]))


bell = Bellman(5)
bell.make_graph(0, 1, -1)
bell.make_graph(0, 2, 4)
bell.make_graph(1, 2, 3)
bell.make_graph(1, 3, 2)
bell.make_graph(1, 4, 2)
bell.make_graph(3, 2, 5)
bell.make_graph(3, 1, 1)
bell.make_graph(4, 3, -3)

bell.BellamFord(0)
