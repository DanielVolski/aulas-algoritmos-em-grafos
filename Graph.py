"""
Author: Daniel Flavio Volski Daum
Date: 18/09/2022

This module was created to store representations and algorithms seen
during the "Algoritmos em Grafos" classes with professor Mauro Henrique
Mulati. All the algorithms and representations are based on the
implementetions presented in the part VI from the book Algorithms, by
Thomas Cormen. 
"""
from enum import Enum
from math import inf

class NodeState(Enum):
    """
    Represents the actual state of a node related to the search algorithm
    """
    UNKNOWN = "UNKNOWN"
    DISCOVERED = "DISCOVERED"
    FINISHED = "FINISHED"

    def __str__(self) -> str:
        return f'{self.value}'

class Node:
    """
    Represents a node of a graph
    """
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.distance = inf
        self.parent = None
        self.state = NodeState.UNKNOWN
        self.adj = []
    
    def __repr__(self) -> str:
        return f'Node("{self.name}", {self.distance}, {self.parent}, "{self.state}")'

    def __str__(self) -> str:
        return f'{self.name}'
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            return self.name == __o.name
        return False
    
    def add_adj_node(self, node: 'Node') -> None:
        self.adj.append(node)

class Edge:
    """
    Represents an edge of a graph
    """

    def __init__(self, u: Node, v: Node, w = 1) -> None:
        self.u = u
        self.v = v
        self.w = w
    
    def __repr__(self) -> str:
        return f'Edge({str(self.u)}, {str(self.v)}, {self.w})'
    
    def __str__(self) -> str:
        return f'({str(self.u)}, {str(self.v)}, {self.w})'
    
class Graph:
    """
    Represents a graph. It includes some basic algorithms related to it

    ...

    Attributes
    ---------
    undirectionded : bool
        Indicates if the graph is directioned or undirectioned
    weighted : bool
        Indicates if the graph is weighted
    edges : [Edge]
        A list that contains the edges of the graph
    nodes : [Node]
        A list that contains the nodes of the graph

    Methods
    -------
    add_edge(u: str, v: str, w = 1) -> None
        Add an edge that goes from vertice u to vertice v with weight w    
    """

    def __init__(self, quantity_of_nodes = 1, undirectioned = True, weighted = True) -> None:
        self.undirectioned = undirectioned
        self.weighted = weighted
        self.nodes = []
        for i in range(0, quantity_of_nodes):
            self.nodes.append(Node(i + 1))

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        adjacency_list = {}
        adjacent_nodes = []
        for node in self.nodes:
            adjacent_nodes = []
            for adj in node.adj:
                adjacent_nodes.append(str(adj))
            adjacency_list[str(node)] = adjacent_nodes
        return f'{adjacency_list}'
    
    def add_edge(self, u, v, w = 1) -> None:
        """
        Add an edge that goes from vertice u to vertice v with weight w. If the
        graph is not weighted, than the value passed to w will be ignored.
        """
        if not self.weighted: w = 1
        if u > len(self.nodes) or v > len(self.nodes):
            raise IndexError("u or v are not in the graph")
        else:
            if self.undirectioned:
                self.nodes[u - 1].add_adj_node(v)
                self.nodes[v - 1].add_adj_node(u)
            else:
                self.nodes[u - 1].add_adj_node(v)
        
    def print_edges(self):
        """
        Prints all the edges added at the graph
        """
        print(f'{self.edges}')

    def print_nodes(self):
        """
        Prints all the nodes added at the graph and its adjascents
        """
        print(f'{self.nodes}')