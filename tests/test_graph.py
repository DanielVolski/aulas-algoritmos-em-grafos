import sys, os, unittest

#This is to aceess parent directory and import Graph.py module
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Graph import Graph, Node

class TestEdge(unittest.TestCase):
    def test_add_edges(self):
        graph = Graph()
        graph.add_edge(1, 2)
    
    def test_print_edge(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(3, 2)
        graph.print_edges()
    
    def test_print_edge(self):
        graph = Graph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(3, 2)
        graph.print_nodes()

if __name__ == '__main__':
    graph = Graph(3)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    print(graph)
    #unittest.main()