class newNode(object):

    def __init__(self, name):
        self.name = name
        self.inEdge = []
        self.outEdge = []

    def addOutEdge(self, outEdge):
        self.outEdge.append(outEdge)

    def addInEdge(self, inEdge):
        self.inEdge.append(inEdge)

    def degree(self):
        return len(self.inEdge) + len(self.outEdge)

class siteGraph(object):

    def __init__(self):
        self.graphNodes = []
        self.allEdges = []

    def maxDegree(self):
        return max(self.graphNodes, key=lambda n: n.degree())

    def meanDegree(self):
        # return max(self.graphNodes, key=lambda n: n.degree())
        return 1.0 * sum([n.degree() for n in self.graphNodes]) / len(self.graphNodes)

def initializeGraph(n):  # n is an integer, the number of nodes in the graph
    G = siteGraph()  # Initializes an empty graph, with G.graphNodes set to []
    for i in range(n):
        # newNode takes one parameter, the number of the node
        G.graphNodes.append(newNode(i))
    for i in range(n):
        x = G.graphNodes[i]
        y = G.graphNodes[(i + 1) % n]
        x.addOutEdge(y)
    y.addInEdge(x)
    G.allEdges.append((x, y))
    return G


if __name__ == '__main__':
    maxDegrees, meanDegrees, meanDegreeVariances, meanShortestPaths = [], [], [], []
    n = 9
    graph = initializeGraph(n)
    for nEdges in range(n, n * n, n * n / 10):
        graph.addEdges(nEdges)
        maxDegrees.append(graph.maxDegree())
        meanDegrees.append(graph.meanDegree())
        meanDegreeVariances.append(graph.meanDegreeVariances())
        meanShortestPaths.append(graph.meanShortestPath())
