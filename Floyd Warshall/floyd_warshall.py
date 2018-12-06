class Floyd_Warshall:
    def __init__(self):
        self.V = 0

    def initialize(self, V):
        self.V = V

    def SSSP(self, graph):
        distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        INF = 9999
        print("Single source shortest path: ")
        for i in range(self.V):
            for j in range(self.V):
                if distance[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end=" ")
            print("\n")


if __name__ == '__main__':
    obj = Floyd_Warshall()
    V = 4
    INF = 9999
    graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
            ]
    obj.initialize(V)
    obj.SSSP(graph)
