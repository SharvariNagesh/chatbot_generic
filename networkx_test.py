import networkx as nx
import matplotlib.pyplot as plt

G= nx.Graph()
G.add_nodes_from([1,2])

G=nx.Graph(name='abc')
print(G.graph)

print(list(G.nodes))

G.add_node("spam")    # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
print(list(G.nodes))
print(G.number_of_nodes())
print(G.number_of_edges())
print(list(G.nodes))
print(list(G.edges))

#----
G.add_nodes_from([1,2,3,4,5,6])
print(list(G.adj[1]))
print(list(G.nodes))
print(G.number_of_nodes())
print(G.number_of_edges())
print(list(G.nodes))
G.add_edge(1, 2)
G[1][2]['color'] = "blue"
G.add_edges_from([(1,3),(1,6)])
G.edges[1, 3]['color'] = "red"
print(list(G.edges))
print(list(G.edges))

class Node:
  x=10
  y=5


n = Node()

G.add_node(n)
print(list(G.nodes))
