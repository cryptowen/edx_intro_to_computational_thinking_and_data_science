class Node(object):

    def __init__(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return str(self.src) + '->' + str(self.dest)


class WeightedEdge(Edge):

    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)


class Digraph(object):

    def __init__(self):
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]


class Graph(Digraph):

    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


def ex1():
    nodes = []
    nodes.append(Node("ABC"))  # nodes[0]
    nodes.append(Node("ACB"))  # nodes[1]
    nodes.append(Node("BAC"))  # nodes[2]
    nodes.append(Node("BCA"))  # nodes[3]
    nodes.append(Node("CAB"))  # nodes[4]
    nodes.append(Node("CBA"))  # nodes[5]

    g = Graph()
    for n in nodes:
        g.addNode(n)

    # for n1 in nodes:
    #     for n2 in nodes:
    #         if n1 != n2 and any(iterable)
    from itertools import combinations
    for n1, n2 in combinations(nodes, 2):
        if any([n1.getName()[i] == n2.getName()[i] for i in [0, -1]]):
            g.addEdge(Edge(n1, n2))
    print g
    # print len(g.edges)



if __name__ == '__main__':
    ex1()
