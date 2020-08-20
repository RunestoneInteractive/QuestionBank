.. activecode:: pythondfs0
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Graphs
    :subchapter: GeneralDepthFirstSearch
    :topics: Graphs/GeneralDepthFirstSearch
    :from_source: T
    :language: python3
    :optional:

    from pythonds.graphs import Graph

    class DFSGraph(Graph):
        def __init__(self):
            super().__init__()
            self.time = 0

        def dfs(self):
            for aVertex in self:
                aVertex.setColor('white')
                aVertex.setPred(-1)
            for aVertex in self:
                if aVertex.getColor() == 'white':
                    self.dfsvisit(aVertex)

        def dfsvisit(self,startVertex):
            startVertex.setColor('gray')
            print("Visiting vertex with ID# " + str(startVertex.id))

            self.time += 1
            startVertex.setDiscovery(self.time)
            for nextVertex in startVertex.getConnections():
                if nextVertex.getColor() == 'white':
                    nextVertex.setPred(startVertex)
                    self.dfsvisit(nextVertex)
            startVertex.setColor('black')
            self.time += 1
            startVertex.setFinish(self.time)

    def main():
        graph = DFSGraph()

        graph.addEdge(0, 1)
        graph.addEdge(0, 2)
        graph.addEdge(0, 5)

        graph.addEdge(3, 4)
        graph.addEdge(3, 2)

        graph.addEdge(1, 5)
        graph.addEdge(1, 2)

        graph.addEdge(5, 4)
        graph.addEdge(5, 3)

        graph.dfs()

    main()