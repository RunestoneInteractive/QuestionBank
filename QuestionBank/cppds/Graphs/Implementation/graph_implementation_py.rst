.. activecode:: graph_implementation_py
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Graphs
  :subchapter: Implementation
  :topics: Graphs/Implementation
  :from_source: T
  :caption: Graph and Vertex implementation
  :optional:

  class Vertex:
        # Contructor that specifies the key of the vertex.
    def __init__(self, key):
            self.id = key
            self.connectedTo = {}
            # Adds a neighbor with the specified weight.
    def addNeighbor(self, nbr, weight=0):
            self.connectedTo[nbr] = weight

            # Converts this vertex to a string representation.
    def __str__(self):
            return str(self.id) + ' connectedTo: ' + str(
                [x.id for x in self.connectedTo])

            # Returns the list of vertex IDs that are connected to this one.
    def getConnections(self):
            return self.connectedTo.keys()

            # Returns the ID of this vertex.
    def getId(self):
            return self.id

            # Returns the weight of this vertex in relation to the specified neighbor.
    def getWeight(self, nbr):
            return self.connectedTo[nbr]


  class Graph:
            # Empty constructor.
    def __init__(self):
            self.vertList = {}
            self.numVertices = 0
            # Adds a vertex with the specified ID (key) and returns it.
    def addVertex(self, key):
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex
            # Returns the vertex (or None if nonexistant) with the specified ID n.
    def getVertex(self, n):
            if n in self.vertList:
                    return self.vertList[n]
            else:
                    return None

            # Returns a boolean indicating if the specified vertex ID is in this graph.
    def __contains__(self, n):
            return n in self.vertList

            # Adds an edge between F and T with a weight of cost.
    def addEdge(self, f, t, cost=0):
            if f not in self.vertList:
                    self.addVertex(f)
            if t not in self.vertList:
                    self.addVertex(t)
            self.vertList[f].addNeighbor(self.vertList[t], cost)

            # Returns a list of all vertices in this graph.
    def getVertices(self):
            return self.vertList.keys()

            # Iteration overload (useful in python).
    def __iter__(self):
            return iter(self.vertList.values())


  def main():
    g = Graph()
    for i in range(6):
            g.addVertex(i)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
            for w in v.getConnections():
                    print("( %s , %s )" % (v.getId(), w.getId()))


  main()